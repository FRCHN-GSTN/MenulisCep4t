'use strict';

const path = require('path');
const { spawnSync } = require('child_process');

function run(argv = []) {
  const isWin = process.platform === 'win32';
  const packageRoot = path.join(__dirname, '..');

  if (argv.includes('--docker')) {
    console.log('Menjalankan verifikasi lingkungan Docker...');
    spawnSync('docker', ['run', '--rm', '-v', `${process.cwd()}:/workspace`, 'muadzhdz/laporan-generator', '--help'], { stdio: 'inherit' });
    return;
  }

  if (argv.includes('--nix')) {
    console.log('Menjalankan via Nix Flake...');
    spawnSync('nix', ['develop', '--command', './test.sh'], { stdio: 'inherit' });
    return;
  }

  if (isWin) {
    const psScript = path.join(packageRoot, 'scripts/setup-deps.ps1');
    const proc = spawnSync('powershell', ['-ExecutionPolicy', 'Bypass', '-File', psScript], { stdio: 'inherit' });
    process.exit(proc.status || 0);
  } else {
    const shScript = path.join(packageRoot, 'scripts/setup-deps.sh');
    const proc = spawnSync('bash', [shScript], { stdio: 'inherit' });
    process.exit(proc.status || 0);
  }
}

module.exports = { run };
