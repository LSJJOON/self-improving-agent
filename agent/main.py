"""
Self-Improving Agent - 핵심 CLI 진입점
사용법: python -m agent run
"""
import argparse
import subprocess
import sys
from pathlib import Path


def find_repo_root() -> Path:
    """Git 레포의 루트 디렉토리를 반환합니다."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        )
        return Path(result.stdout.strip())
    except subprocess.CalledProcessError:
        return Path.cwd()


def read_backlog(repo_root: Path):
    """BACKLOG.md를 읽어 내용을 반환합니다."""
    backlog_path = repo_root / "BACKLOG.md"
    if not backlog_path.exists():
        return None, "BACKLOG.md를 찾을 수 없습니다."
    return backlog_path.read_text(encoding="utf-8"), None


def select_task(backlog_content: str):
    """백로그에서 다음 미완료 작업을 선택합니다."""
    for line in backlog_content.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [ ]"):
            return stripped[5:].strip()
    return None


def cmd_run(args):
    """에이전트를 실행합니다."""
    print("🤖 Self-Improving Agent 시작...\n")

    repo_root = find_repo_root()
    if args.verbose:
        print(f"📁 레포 루트: {repo_root}")

    backlog_content, err = read_backlog(repo_root)
    if err:
        print(f"❌ 오류: {err}")
        sys.exit(1)

    task = select_task(backlog_content)
    if not task:
        print("✅ 모든 백로그 항목이 완료되었습니다! 새 항목을 추가해 주세요.")
        return

    print(f"📋 선택된 작업: {task}")

    if args.dry_run:
        print("\n[dry-run] 실제 변경 없이 시뮬레이션 완료.")
        return

    print("\n⚙️  작업을 분석 중... (Claude API 연동 시 자동 구현됩니다)")
    print("✨ 실행 완료. 다음 단계: PR 생성 및 BACKLOG 업데이트")


def cmd_status(args):
    """현재 백로그 상태를 출력합니다."""
    repo_root = find_repo_root()
    backlog_content, err = read_backlog(repo_root)
    if err:
        print(f"❌ {err}")
        sys.exit(1)

    lines = backlog_content.splitlines()
    pending = [l.strip()[5:].strip() for l in lines if l.strip().startswith("- [ ]")]
    done = [l.strip()[5:].strip() for l in lines if l.strip().startswith("- [x]")]

    print("📊 백로그 현황")
    print(f"   ✅ 완료: {len(done)}개")
    print(f"   ⏳ 대기: {len(pending)}개")
    if pending:
        print(f"\n   🔜 다음 작업: {pending[0]}")
        if args.verbose and len(pending) > 1:
            for t in pending[1:4]:
                print(f"   ▫  {t}")


def main():
    parser = argparse.ArgumentParser(
        description="Self-Improving Agent — 자율 코드 개선 에이전트",
        prog="agent",
    )
    sub = parser.add_subparsers(dest="command", metavar="<command>")

    # run
    p_run = sub.add_parser("run", help="에이전트를 실행합니다")
    p_run.add_argument("-v", "--verbose", action="store_true", help="상세 출력")
    p_run.add_argument("--dry-run", action="store_true", help="변경 없이 시뮬레이션")

    # status
    p_status = sub.add_parser("status", help="백로그 현황을 확인합니다")
    p_status.add_argument("-v", "--verbose", action="store_true", help="대기 작업 목록 출력")

    args = parser.parse_args()

    if args.command == "run":
        cmd_run(args)
    elif args.command == "status":
        cmd_status(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
