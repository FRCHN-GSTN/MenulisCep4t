'use strict';

const fs = require('fs');
const path = require('path');
const os = require('os');

function removeRecursiveSync(targetPath) {
  if (!fs.existsSync(targetPath)) return;
  try {
    const stats = fs.statSync(targetPath);
    if (stats.isDirectory()) {
      fs.readdirSync(targetPath).forEach((child) => {
        removeRecursiveSync(path.join(targetPath, child));
      });
      fs.rmdirSync(targetPath);
    } else {
      fs.unlinkSync(targetPath);
    }
  } catch (err) {
    // ignore
  }
}

function parseJsonc(content) {
  const clean = content
    .replace(/^\s*\/\/.*$/gm, '')
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .trim();
  return JSON.parse(clean);
}

function run(argv = []) {
  const home = os.homedir();

  console.log('\n==========================================================');
  console.log('   LAPORAN GENERATOR - PEMBERSIHAN & UNINSTALL SKILLS     ');
  console.log('==========================================================\n');

  // 1. Hapus dari skills direktori (baik laporan-generator maupun alias laporan)
  const skillDirs = [
    path.join(home, '.agents/skills/laporan-generator'),
    path.join(home, '.agents/skills/laporan'),
    path.join(home, '.gemini/config/skills/laporan-generator'),
    path.join(home, '.gemini/config/skills/laporan'),
    path.join(home, '.claude/skills/laporan-generator'),
    path.join(home, '.claude/skills/laporan'),
    path.join(home, '.grok/skills/laporan-generator'),
    path.join(home, '.grok/skills/laporan'),
    path.join(home, '.config/opencode/skills/laporan-generator'),
    path.join(home, '.config/opencode/skills/laporan')
  ];

  for (const sDir of skillDirs) {
    if (fs.existsSync(sDir)) {
      removeRecursiveSync(sDir);
      console.log(`  ✔ [REMOVED] Skill: ${sDir}`);
    }
  }

  // 2. Hapus Kiro CLI agents
  const kiroAgents = [
    path.join(home, '.kiro/agents/laporan-generator.json'),
    path.join(home, '.kiro/agents/laporan.json')
  ];
  for (const kAgent of kiroAgents) {
    if (fs.existsSync(kAgent)) {
      removeRecursiveSync(kAgent);
      console.log(`  ✔ [REMOVED] Kiro Agent: ${kAgent}`);
    }
  }

  // 3. Hapus Workflows & Slash Commands
  const workflowFiles = [
    path.join(home, '.agents/workflows/laporan-generator.md'),
    path.join(home, '.agents/workflows/laporan.md'),
    path.join(home, '.claude/commands/laporan-generator.md'),
    path.join(home, '.claude/commands/laporan.md')
  ];
  for (const wFile of workflowFiles) {
    if (fs.existsSync(wFile)) {
      removeRecursiveSync(wFile);
      console.log(`  ✔ [REMOVED] Command / Workflow: ${wFile}`);
    }
  }

  // 4. Bersihkan OpenCode config (~/.config/opencode/opencode.jsonc)
  const opencodeConfigPath = path.join(home, '.config/opencode/opencode.jsonc');
  if (fs.existsSync(opencodeConfigPath)) {
    try {
      const raw = fs.readFileSync(opencodeConfigPath, 'utf8');
      let opencodeConfig = parseJsonc(raw);
      let modified = false;

      if (opencodeConfig.command) {
        if (opencodeConfig.command['laporan']) {
          delete opencodeConfig.command['laporan'];
          modified = true;
        }
        if (opencodeConfig.command['laporan-generator']) {
          delete opencodeConfig.command['laporan-generator'];
          modified = true;
        }
        if (Object.keys(opencodeConfig.command).length === 0) {
          delete opencodeConfig.command;
        }
        modified = true;
      }

      if (modified) {
        fs.writeFileSync(opencodeConfigPath, JSON.stringify(opencodeConfig, null, 2), 'utf8');
        console.log(`  ✔ [CLEANED] OpenCode config (~/.config/opencode/opencode.jsonc)`);
      }
    } catch (err) {
      console.log(`  ✖ [OPENCODE CLEAN ERROR] ${err.message}`);
    }
  }

  // 5. Bersihkan registrasi MCP Server
  const mcpConfigs = [
    path.join(home, '.gemini/config/mcp_config.json'),
    path.join(home, '.claude.json'),
    path.join(home, '.config/Claude/claude_desktop_config.json')
  ];
  for (const mcpFile of mcpConfigs) {
    if (fs.existsSync(mcpFile)) {
      try {
        const raw = fs.readFileSync(mcpFile, 'utf8');
        const data = JSON.parse(raw);
        if (data.mcpServers && (data.mcpServers['laporan'] || data.mcpServers['laporan-generator'])) {
          delete data.mcpServers['laporan'];
          delete data.mcpServers['laporan-generator'];
          fs.writeFileSync(mcpFile, JSON.stringify(data, null, 2), 'utf8');
          console.log(`  ✔ [CLEANED MCP] Removed laporan server from: ${mcpFile}`);
        }
      } catch (_) {}
    }
  }

  console.log('\n==========================================================');
  console.log('✨ Uninstall selesai! Seluruh integrasi AI agent telah dibersihkan.');
  console.log('==========================================================\n');
}

module.exports = { run, removeRecursiveSync, parseJsonc };
