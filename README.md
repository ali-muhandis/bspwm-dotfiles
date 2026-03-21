<h1 align="center">Arch Linux + bspwm Dotfiles</h1>

<p align="center">
  <b>A fully configured Arch Linux desktop environment with bspwm, Catppuccin Mocha theme, and automated installer.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/OS-Arch%20Linux-1793D1?style=for-the-badge&logo=archlinux&logoColor=white">
  <img src="https://img.shields.io/badge/WM-bspwm-89B4FA?style=for-the-badge">
  <img src="https://img.shields.io/badge/Theme-Catppuccin%20Mocha-1E1E2E?style=for-the-badge">
</p>

---

## Overview

| Component | Tool |
|---|---|
| **OS** | [Arch Linux](https://archlinux.org/) |
| **WM** | [bspwm](https://github.com/baskerville/bspwm) |
| **Bar** | [Polybar](https://github.com/polybar/polybar) |
| **Compositor** | [Picom](https://github.com/yshui/picom) |
| **Terminal** | [Alacritty](https://github.com/alacritty/alacritty) |
| **Shell** | [Fish](https://fishshell.com/) + [Starship](https://starship.rs/) |
| **Multiplexer** | [tmux](https://github.com/tmux/tmux) |
| **Editor** | [Neovim](https://neovim.io/) (lazy.nvim) |
| **Launcher** | [Rofi](https://github.com/davatorium/rofi) |
| **Notifications** | [Dunst](https://github.com/dunst-project/dunst) |
| **File Manager** | [Thunar](https://docs.xfce.org/xfce/thunar/start) + [Ranger](https://ranger.github.io/) |
| **Login Manager** | [SDDM](https://github.com/sddm/sddm) (Astronaut theme) |
| **Audio** | [PipeWire](https://pipewire.org/) + WirePlumber |
| **Database** | [PostgreSQL](https://www.postgresql.org/) |
| **Firewall** | [UFW](https://wiki.archlinux.org/title/Uncomplicated_Firewall) |

## Theme

**Catppuccin Mocha** (blue accent) applied consistently across:

- GTK 2/3/4 — `catppuccin-mocha-blue-standard+default`
- Cursors — `catppuccin-mocha-blue-cursors`
- Icons — `Papirus-Dark`
- Terminal — Catppuccin Mocha colors
- Neovim — Catppuccin colorscheme
- tmux — Custom Catppuccin status bar
- Firefox — Custom userChrome.css
- SDDM — Astronaut theme with Catppuccin colors
- GRUB — Catppuccin Mocha + Arch Linux logo
- i3lock — Catppuccin colors with wallpaper background
- btop — Catppuccin Mocha theme

## Features

- **Automated installer** — single `python3 install.py` sets up everything
- **tmux** — Ctrl+a prefix, vim-style navigation, auto-save sessions, homepage with Arch logo
- **Neovim** — LSP (pyright, ts_ls, rust_analyzer, ruff), autocomplete, treesitter, telescope
- **Fish shell** — zoxide (smart cd), fzf (fuzzy finder), eza (modern ls), starship prompt
- **Polybar** — workspaces, CPU, memory, temperature, battery, backlight, volume, clock, keyboard layout
- **Picom** — blur, shadows, rounded corners, fading animations
- **Screen lock** — i3lock-color with Catppuccin theme, auto-centered
- **30+ utility scripts** — volume, brightness, powermenu, random wallpaper, wifi menu, calculator, timer
- **SSH agent** — auto-loads keys on shell startup
- **PostgreSQL** — auto-configured with user superuser
- **Timeshift** — weekly system backups via cronie

## Keybindings

### General
| Key | Action |
|---|---|
| `Super + Enter` | Terminal (Alacritty) |
| `Super + d` | App launcher (Rofi) |
| `Super + c` | Close window |
| `Super + x` | Powermenu |
| `Super + w` | Random wallpaper |
| `Super + p` | Toggle Polybar |
| `Super + Space` | Toggle floating/tiled |
| `Super + f` | Fullscreen |
| `Super + 1-9` | Switch workspace |
| `Super + Shift + 1-9` | Move window to workspace |
| `Alt + Shift` | Change keyboard layout (US/RU) |
| `Print` | Screenshot (Flameshot) |
| `Ctrl + Shift + q` | Quit bspwm |
| `Ctrl + Shift + r` | Restart bspwm |

### tmux (prefix: Ctrl+a)
| Key | Action |
|---|---|
| `Ctrl+a \|` | Vertical split |
| `Ctrl+a -` | Horizontal split |
| `Ctrl+a h/j/k/l` | Navigate panes |
| `Ctrl+a c` | New window |
| `Ctrl+a n/p` | Next/previous window |
| `Ctrl+a ,` | Rename window |
| `Ctrl+a $` | Rename session |
| `Ctrl+a d` | Detach session |
| `Ctrl+a s` | List sessions |
| `Ctrl+a r` | Reload config |
| `Ctrl+a Space` | tmux-thumbs (select text) |
| `Ctrl+a f` | tmux-fzf (fuzzy finder) |
| `Ctrl+a Ctrl+s` | Save session |
| `Ctrl+a Ctrl+r` | Restore session |

### Super + Shift — Applications
| Key | App |
|---|---|
| `f` | Firefox |
| `n` | Thunar |
| `p` | Pavucontrol |
| `t` | Telegram |
| `c` | Calculator |
| `i` | Firefox Private |
| `l` | Screen Lock |
| `e` | Emoji Picker |
| `s` | Timer |
| `k` | Calcurse |

## Installation

### Prerequisites
- Fresh Arch Linux installation with base system
- Internet connection
- Git installed

### Quick Install

```bash
git clone https://github.com/your-username/bspwm-dotfiles.git ~/bspwm-dotfiles
cd ~/bspwm-dotfiles/Builder
python3 install.py
```

The installer will ask 4 questions:
1. **Install dotfiles?** — copies all configs to `~/.config/`
2. **Update Arch database?** — runs `pacman -Syu`
3. **Install BSPWM dependencies?** — installs all packages
4. **Install dev dependencies?** — installs dev tools (VS Code, OBS, etc.)

### Post-install

After installation, reboot and select bspwm from SDDM login screen.

```bash
sudo reboot
```

## Directory Structure

```
bspwm-dotfiles/
├── Builder/              # Automated installer
│   ├── install.py        # Entry point
│   ├── packages.py       # Package lists
│   ├── options.py        # User interface
│   ├── logger.py         # Logging system
│   └── creators/         # Installation modules
├── config/               # All ~/.config/ files
│   ├── alacritty/        # Terminal config
│   ├── bspwm/            # Window manager
│   ├── fish/             # Shell config
│   ├── nvim/             # Neovim config
│   ├── polybar/          # Status bar
│   ├── picom/            # Compositor
│   ├── rofi/             # Launcher
│   ├── sxhkd/            # Keybindings
│   ├── btop/             # System monitor
│   ├── gtk-2.0/3.0/4.0/  # GTK themes
│   └── ...
├── bin/                  # Utility scripts
├── sddm/                # Login screen theme
├── themes/               # GTK themes
├── firefox/              # Browser customization
├── Images/               # Wallpapers
├── .tmux.conf            # tmux configuration
├── Xresources            # X11 settings
├── xinitrc               # X11 init
└── gtkrc-2.0             # GTK2 config
```

## Font Stack

| Usage | Font |
|---|---|
| Terminal / Polybar / Code | JetBrainsMono Nerd Font |
| System UI (GTK) | Noto Sans |
| Browser content | Page default fonts |

## Credits

- Based on [ZProger/bspwm-dotfiles](https://github.com/zproger/bspwm-dotfiles)
- Theme: [Catppuccin](https://github.com/catppuccin/catppuccin)
- SDDM Theme: [sddm-astronaut-theme](https://github.com/Keyitdev/sddm-astronaut-theme)
