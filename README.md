# MPV Config by Pololer

A powerful and customizable configuration preset for [MPV Media Player](https://mpv.io/). This setup enhances your MPV experience with advanced features, optimized settings, and a sleek interface.

---

## ✨ Features

- **Custom UI Enhancements**: Includes modern and intuitive UI elements for better usability.
- **Auto-Cropping**: Automatically detects and crops black bars in videos.
- **Cover Art Display**: Displays album or video cover art when available.
- **Advanced Audio Filters**: Fine-tune your audio with custom filters.
- **Screenshot Mosaic**: Generate beautiful mosaic screenshots of your videos.
- **Video Thumbnails**: Quickly preview video scenes with thumbnail generation.
- **WebTorrent Support**: Stream torrents directly in MPV.
- **Performance Optimizations**: Tweaked settings for smooth playback and reduced resource usage.
- **Shader Support**: Includes shaders for improved video quality.

---

## 📸 Preview

![Screenshot 1](https://github.com/user-attachments/assets/55e595bd-5a07-409f-9863-ec82476d0600)
![Screenshot 2](https://github.com/user-attachments/assets/8723670b-674a-4ff2-92b2-83aa5992ea08)

---

## 🚀 Installation Guide

### Portable Config
1. Download the repository as a ZIP file and extract it.
2. Copy the contents of the extracted folder to the `portable_config` folder in your MPV directory.

### AppData (Windows)
1. Download the repository as a ZIP file and extract it.
2. Copy the contents of the extracted folder to `%AppData%\mpv\`.

### Linux
1. Download the repository as a ZIP file and extract it.
2. Copy the contents of the extracted folder to `~/.config/mpv/`.

### Using Git Clone
1. Open a terminal.
2. Navigate to the desired directory:
    ```sh
    cd ~/.config/mpv/
    ```
3. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git .
    ```
4. Ensure the contents are in the correct directory.

---

## ⚙️ Configuration Options

You can customize the behavior of this configuration by editing the files in the `script-opts` folder. Below are some key options:

- **`coverart.conf`**: Configure cover art display settings.
- **`crop.conf`**: Adjust auto-cropping behavior.
- **`stats.conf`**: Customize the on-screen statistics display.
- **`thumbfast.conf`**: Modify thumbnail generation settings.
- **`uosc.conf`**: Personalize the user interface.

---

## 🛠️ Requirements

- [MPV Media Player](https://mpv.io/)
- [Lua](https://www.lua.org/) (for custom scripts)
- Optional: GPU with shader support for enhanced video quality.

---

## 📂 Folder Structure
```
mpv-config/
├── cover/         # Cover art assets
├── fonts/         # Custom fonts for UI
├── script-opts/   # Configuration files for scripts
├── scripts/       # Lua scripts for added functionality
├── shaders/       # Video shaders for quality improvements
├── src/           # Source files for advanced features
├── tests/         # Test scripts and configurations
└── vs-scripts/    # VapourSynth scripts (if applicable)
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this configuration.

---

Enjoy your enhanced MPV experience! 🎥

![MPV UI](https://cdn.lewd.host/txrWjaOE.png)