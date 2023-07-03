import AdmZip from 'adm-zip';
import { resolve } from 'path';
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
import config from './config.json';

const args = yargs(hideBin(process.argv))
  .command('bun release.ts', 'bundle the mod into a zip file', yargs => {
      return yargs
        .option('include', {
            describe: 'include another mod',
            type: 'string',
        });
  })
  .parseSync()

const adm = new AdmZip();
adm.addLocalFolder('./modules', 'python-packages');
adm.addLocalFolder('./assets', `mods/${config.injected_name}`);
// @ts-expect-error - find correct types for args.include
adm.addLocalFolder(resolve(process.cwd(), args.include, 'assets'), `mods/${args._[0]}`);
adm.writeZip(`./build/${config.name} Mod ${config.versions.mod} for ${config.versions.game}.zip`);
