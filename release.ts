import AdmZip from 'adm-zip';
import { resolve } from 'path';
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
import config from './config.json';

const toUpperCase = (text: string) => text[0].toUpperCase() + text.slice(1);

const args = yargs(hideBin(process.argv))
  .command('bun release.ts', 'bundle the mod into a zip file', (yargs) => {
    return yargs.option('include', {
      describe: 'include another mod',
      type: 'string',
    });
  })
  .parseSync();

const isString = (text: unknown): text is string => typeof text === 'string';

const adm = new AdmZip();
adm.addLocalFolder(
  './modules',
  resolve('python-packages', config.injected_name)
);
adm.addLocalFolder('./assets', `mods/${config.injected_name}`);

const include = args.include;
const name = args._[0];
const isPartOfBundle = isString(include);
const hasName = isString(name);
const buildName = [
  config.name,
  'mod',
  config.versions.mod,
  'for',
  config.versions.game,
  hasName ? `with ${toUpperCase(name)} included` : '',
];

if (isPartOfBundle)
  adm.addLocalFolder(resolve(process.cwd(), include, 'assets'), `mods/${name}`);

adm.writeZip(resolve(process.cwd(), 'build', `${buildName.join(' ')}.zip`));
