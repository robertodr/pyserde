import sys

import collection
import default
import env
import jsonfile
import rename
import simple
import skip
import tomlfile
import union
import yamlfile


def run_all():
    run(simple)
    run(collection)
    run(default)
    run(env)
    run(rename)
    run(skip)
    run(jsonfile)
    run(tomlfile)
    run(yamlfile)
    run(union)


def run(module):
    print('-----------------')
    print(f'running {module.__name__}')
    module.main()


if __name__ == '__main__':
    try:
        run_all()
    except Exception:
        sys.exit(1)