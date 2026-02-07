// ═══════════════════════════════════════════════════════════════
//  FORGED BANNER — ASCII Glitch Animator
//  forged.itsbroken.ai / Cipher Circle
//  Based on the itsbroken.ai BrokenCover engine
// ═══════════════════════════════════════════════════════════════

const _W = 76;
const _p = s => s.padEnd(_W).slice(0, _W);

const FORGED_BANNER = [
  _p(''),
  _p('          ███████████████████████'),
  _p('          ███                 ███'),
  _p('     ████████  █████   █████  ████████'),
  _p('██████████       █████   █████        ██████████'),
  _p('██                                              ██'),
  _p('██   ███████   █████████████████   ████████     ██'),
  _p('██   ██   ██   ██             ██   ███  ███     ██'),
  _p('███████   ██   █████       █████   ███  ████████'),
  _p('          ██     ███       ███     ███'),
  _p('          ██████████       ███████████'),
  _p(''),
];

// ─────────────────────────────────────────────────────────────
//  GLITCH ENGINE (from itsbroken.ai BrokenCover)
// ─────────────────────────────────────────────────────────────

const GLITCH_CHARS = '░▒▓█▀▄╔╗╚╝║═┃━┏┓┗┛';
const CORRUPTION_CHARS = '!@#$%^&*<>{}[]|/\\~`';

class ForgedBanner {
  constructor(element, baseFrame) {
    this.el = element;
    this.base = baseFrame;
    this.lines = baseFrame.slice();
    this.width = baseFrame[0].length;
    this.height = baseFrame.length;
    this.frame = 0;
    this.glitchIntensity = 0;
    this.phase = 'stable';
    this.phaseTimer = 0;
    this.playing = true;
    this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  glitchChar() {
    const pool = Math.random() > 0.5 ? GLITCH_CHARS : CORRUPTION_CHARS;
    return pool[Math.floor(Math.random() * pool.length)];
  }

  corruptLine(line, intensity) {
    const chars = [...line];
    const corruptions = Math.floor(intensity * chars.length * 0.25);
    for (let i = 0; i < corruptions; i++) {
      const pos = Math.floor(Math.random() * chars.length);
      const action = Math.random();
      if (action < 0.4) {
        chars[pos] = this.glitchChar();
      } else if (action < 0.7) {
        const len = Math.floor(Math.random() * 6) + 1;
        const shift = Math.floor(Math.random() * 4) - 2;
        for (let j = 0; j < len && pos + j < chars.length; j++) {
          const src = pos + j + shift;
          if (src >= 0 && src < chars.length) {
            chars[pos + j] = line[src] || this.glitchChar();
          }
        }
      } else {
        const len = Math.floor(Math.random() * 4) + 1;
        const fillChar = '░▒▓█'[Math.floor(Math.random() * 4)];
        for (let j = 0; j < len && pos + j < chars.length; j++) {
          chars[pos + j] = fillChar;
        }
      }
    }
    return chars.join('');
  }

  horizontalTear(lines, startRow, numRows, offset) {
    for (let i = startRow; i < startRow + numRows && i < lines.length; i++) {
      const line = lines[i];
      if (offset > 0) {
        lines[i] = ' '.repeat(offset) + line.slice(0, -offset);
      } else if (offset < 0) {
        lines[i] = line.slice(-offset) + ' '.repeat(-offset);
      }
    }
  }

  render() {
    this.frame++;
    this.phaseTimer++;

    // Phase state machine
    if (this.phase === 'stable' && this.phaseTimer > 100) {
      if (Math.random() < 0.12) {
        this.phase = 'glitch';
        this.phaseTimer = 0;
        this.glitchIntensity = 0.08 + Math.random() * 0.3;
      }
    } else if (this.phase === 'glitch') {
      if (this.phaseTimer > 8 + Math.random() * 16) {
        if (Math.random() < 0.25) {
          this.phase = 'heavy';
          this.phaseTimer = 0;
          this.glitchIntensity = 0.4 + Math.random() * 0.4;
        } else {
          this.phase = 'recover';
          this.phaseTimer = 0;
        }
      }
    } else if (this.phase === 'heavy') {
      if (this.phaseTimer > 3 + Math.random() * 6) {
        this.phase = 'recover';
        this.phaseTimer = 0;
      }
    } else if (this.phase === 'recover') {
      this.glitchIntensity *= 0.7;
      if (this.glitchIntensity < 0.01) {
        this.phase = 'stable';
        this.phaseTimer = 0;
        this.glitchIntensity = 0;
      }
    }

    let lines = this.base.slice();

    if (this.glitchIntensity > 0.01) {
      const numCorrupted = Math.floor(this.height * this.glitchIntensity * 0.5);
      for (let i = 0; i < numCorrupted; i++) {
        const row = Math.floor(Math.random() * this.height);
        lines[row] = this.corruptLine(this.base[row], this.glitchIntensity);
      }

      if (Math.random() < this.glitchIntensity * 0.7) {
        const tearRow = Math.floor(Math.random() * this.height);
        const tearHeight = 1 + Math.floor(Math.random() * 2);
        const tearOffset = Math.floor((Math.random() - 0.5) * 10);
        this.horizontalTear(lines, tearRow, tearHeight, tearOffset);
      }

      if (Math.random() < this.glitchIntensity * 0.15) {
        const row = Math.floor(Math.random() * this.height);
        const char = '░▒▓█'[Math.floor(Math.random() * 4)];
        lines[row] = char.repeat(this.width);
      }

      // Color flash — amber palette only
      if (Math.random() < this.glitchIntensity * 0.25) {
        const colors = ['#C65D07', '#D4A84B', '#ff6b35', '#e8963a'];
        this.el.style.color = colors[Math.floor(Math.random() * colors.length)];
        setTimeout(() => { this.el.style.color = '#D4A84B'; }, 50);
      }
    }

    // Micro-glitches during stable
    if (this.phase === 'stable' && Math.random() < 0.02) {
      const row = Math.floor(Math.random() * this.height);
      const col = Math.floor(Math.random() * this.width);
      const chars = [...lines[row]];
      if (chars[col] && chars[col] !== ' ') {
        chars[col] = this.glitchChar();
        lines[row] = chars.join('');
      }
    }

    this.el.textContent = lines.join('\n');
  }

  start() {
    if (this.reducedMotion) {
      this.el.textContent = this.base.join('\n');
      return;
    }
    const loop = () => {
      if (!this.playing) return;
      this.render();
      setTimeout(() => requestAnimationFrame(loop), 1000 / 20);
    };
    loop();
  }
}

// ─────────────────────────────────────────────────────────────
//  BOOT
// ─────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', function() {
  const canvas = document.getElementById('forged-banner');
  if (!canvas) return;
  const banner = new ForgedBanner(canvas, FORGED_BANNER);
  banner.start();
});
