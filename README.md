# SublimeLinter-contrib-healthier

A linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) to integrate [Healthier Linter](https://github.com/KidkArolis/healthier).

## Installation

Install `SublimeLinter` and `SublimeLinter-contrib-healthier` using [Package Control](https://packagecontrol.io).

Then, ensure that `healthier` is installed as your project dependency:

```
$ npm install -D healthier
```

If `healthier` is installed in the project as a dev dependency, the SublimeLinter should have no trouble finding it. If you have issues, make sure to check out [troubleshooting PATH configuration](https://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings

- [SublimeLinter settings](https://sublimelinter.readthedocs.org/en/latest/settings.html)
- [Linter settings](https://sublimelinter.readthedocs.org/en/latest/linter_settings.html)

## Note

Healthier linting is only enabled for projects with `healthier` in `devDependencies`/`dependencies` in package.json.
