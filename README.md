# SublimeLinter-contrib-healthier

A linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) to integrate [Healthier Linter](https://github.com/KidkArolis/healthier).

## Installation

**Important**

The Package has not been merged into SublimeLinter yet. So in the meantime, to install you can do the following:

1. `Cmd+Shift+P` and pick `Add repository`
2. Enter `https://github.com/KidkArolis/SublimeLinter-contrib-healthier`
3. `Cmd+Shift+P` and pick `Install package`
4. Search for `healthier`

Should be good to go!

**In the future**

SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `healthier` is installed as your project dependency:

```
$ npm install healthier
```

If `healthier` is installed in the project as a dev dependency, the SublimeLinter should have no trouble finding it. If you have issues, make sure to check out [troubleshooting PATH configuration](https://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings

- [SublimeLinter settings](https://sublimelinter.readthedocs.org/en/latest/settings.html)
- [Linter settings](https://sublimelinter.readthedocs.org/en/latest/linter_settings.html)

## Note

Healthier linting is only enabled for projects with `healthier` in `devDependencies`/`dependencies` in package.json.

