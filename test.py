import utils
from utils import TESTS, show
from pathlib import Path
import traceback
import importlib
import sys

REPORT = """###### Test Summary #######

EXECUTED = {EXECUTED}
PASSED = {PASSED}
FAILED = {FAILED}
ERRORS = {ERRORS}
SKIPPED = {SKIPPED}
"""

REPORT2 = "executed:{EXECUTED} passed:{PASSED} failed:{FAILED} errors:{ERRORS}"

def test():
    # import each module and run it's tests
    for n in range(1,26):
        module_name = f"day{n}"
        if (Path(__file__).parent / f"{module_name}.py").is_file():
            try:
                print(f"####### Day {n} #######")
                mod = importlib.import_module(module_name)
                show(mod.p1, mod.p2, compact=True)
            except:
                TESTS.ERRORS += 1
                traceback.print_exc()

    # print test report
    print(REPORT2.format(**TESTS.__dict__))

if __name__ == "__main__":
    test()
    sys.exit(TESTS.FAILED)
