import logging
import subprocess
import typing as t

logger = logging.getLogger(__name__)

GIT_TIMEOUT = 3


def get_git_url(git_path: str) -> t.Optional[str]:
    args = ["git", "remote", "-v"]
    output = ""
    try:
        process = subprocess.run(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=git_path,
            timeout=GIT_TIMEOUT,
        )
        output = process.stdout.decode("utf-8")
        err = process.stderr.decode("utf-8")
    except (Exception,) as ex:
        err = str(ex)
    if len(err) > 0:
        logger.warning("git remote -v failed: %s", err.strip())
        return None
    lines = output.split("\n")
    url = None
    for line in lines:
        if "origin" in line:
            buff = line.split()
            url = buff[1]
    return url


def get_git_author_and_repo(
    git_path: str,
) -> tuple[t.Optional[str], t.Optional[str]]:
    author = None
    repo = None
    url = get_git_url(git_path)
    if url is not None:
        buff = url.split("/")
        if len(buff) == 5:
            author = buff[3]
            repo = buff[4]
            repo = repo.split(".")
            repo = repo[0]
    return author, repo


def get_git_branch(git_path: str) -> t.Optional[str]:
    args = ["git", "branch", "-v"]
    output = ""
    try:
        process = subprocess.run(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=git_path,
            timeout=GIT_TIMEOUT,
        )
        output = process.stdout.decode("utf-8")
        err = process.stderr.decode("utf-8")
    except (Exception,) as ex:
        err = str(ex)
    if len(err) > 0:
        logger.warning("git branch -v failed: %s", err.strip())
        return None
    lines = output.split("\n")
    branch = None
    for line in lines:
        if "*" in line:
            buff = line.split()
            branch = buff[1]
    return branch


def get_git_hash(git_path: str, short: bool = False) -> t.Optional[str]:
    args = ["git", "rev-parse", "HEAD"]
    if short:
        args.insert(2, "--short")
    output = ""
    try:
        process = subprocess.run(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=git_path,
            timeout=GIT_TIMEOUT,
        )
        output = process.stdout.decode("utf-8")
        err = process.stderr.decode("utf-8")
    except (Exception,) as ex:
        err = str(ex)
    if len(err) > 0:
        logger.warning("git rev-parse HEAD failed: %s", err.strip())
        return None
    buff = output.split("\n")
    return buff[0]


def get_repo_info(git_path: str) -> dict[str, t.Optional[str]]:
    author, repo = get_git_author_and_repo(git_path)
    return {
        "repo_author": author,
        "repo_name": repo,
        "repo_url": get_git_url(git_path),
        "repo_branch": get_git_branch(git_path),
        "repo_hash": get_git_hash(git_path, short=True),
    }
