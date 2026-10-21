# 月蚀守望 · 美术与音频来源

- Kenney **Tiny Dungeon 1.0** — https://kenney.nl/assets/tiny-dungeon ，CC0。角色、敌人、武器、道具、遗迹建筑。
- Kenney **Tiny Town 1.1** — https://kenney.nl/assets/tiny-town ，CC0。森林、树木、篱笆、地表、弓箭。
- Kenney **RPG Audio** — https://kenney.nl/assets/rpg-audio ，CC0。挥击、开箱、金币、选择和药剂声音。
- 许可原文在 `assets/licenses/`，每个新美术文件与来源的对应关系在 `assets/moonwatch/manifest.json`。
- 四段 `moon_garden/frost/ember/eclipse.ogg` 为本次项目编写的原创合成氛围音乐，随项目按 MIT 许可提供。重建脚本：`tools/generate_music.py`（需要 numpy、soundfile）。
- 新符文圆环、月晶与灵焰由项目的 WGSL 着色器绘制，源码在 `assets/shaders/moon_*.wgsl`。角色步态和呼吸由 `src/anim.rs` 的程序动画提供；素材包本身是单帧角色。
- 未替换的音效沿用原项目 Kenney 音效；字体沿用 Noto Sans CJK SC，其许可见 `assets/fonts/`。
- 原始 0x72 美术仍保留在源码的 `assets/dungeon/` 供溯源，新版加载 `assets/moonwatch/`。
