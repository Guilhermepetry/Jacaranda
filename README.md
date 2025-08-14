# Jacarandá

**Jacarandá** is a personal fork of the [Rosewood Game Engine](https://github.com/dovker/Rosewood), originally created by Dovydas Vaičiukynas.  
The purpose of this fork is purely educational — mainly to study the _Deferred pseudo-3D rendering_ example, which emulates a lighting system similar to the one used in the game [Eastward](https://www.indiedb.com/games/eastward/images/lighting-test).

I recently started studying computer graphics and I am a complete beginner in the field. This project serves as a playground for experimentation and learning.

The name **Jacarandá** is the Portuguese translation of _Rosewood_.

---

## Rosewood Game Engine

**Rosewood Engine** is a game engine developed as a learning project for graphics programming and game engine architecture. While no longer actively maintained, it achieved its primary goals of:

- Providing a framework for creating advanced 2D games
- Supporting basic 3D game development
- Teaching core concepts of engine development
- Implementing modern C++ patterns and graphics programming techniques

## Features

- OpenGL Support
- Cross-Platform (Tested on major desktop platforms)
- 2D Rendering
- Asset management system
- 2D Audio support
- ECS (Entity Component System)
- File system and Compression
- Lua Scripting
- Basic Networking

## Building

### All Platforms

1. Ensure all dependencies have their premake5.lua files (available in `vendor/premakes` if missing)
2. **Important:** Compile OpenSSL in `Rosewood/vendor/openssl` as a Static Library (using `no-shared` option)
3. Use the **Build Tool** located in `Tools/BuildTool.py`

### Windows

1. Generate project files by selecting the project and generator type
2. Open in your preferred IDE or use the Build Tool's **Build** and **Run** buttons for `gmake2`

### MacOS

1. Download Premake5 binaries for MacOS to `vendor/bin/premake`
2. Use Build Tool to create `MakeFiles` or `XCode` files
3. Build via XCode or use MakeFiles with Build Tool

### Linux

1. Download Premake5 binaries for Linux to `vendor/bin/premake`
2. Required packages:
   - `xorg-dev`
   - `libasound2-dev`
3. Use Build Tool to create `MakeFiles`
4. Build and run through the tool

## Screenshots

### Lua Scripting demonstration

All the characters seen on this demonstration are being controled via a Lua Script

https://user-images.githubusercontent.com/29017432/184543662-437f4487-839a-4301-a8f8-e27e1b23cb56.mov

### Deferred pseudo-3D rendering

What you're seeing here is an orthographic projection of 3D paper-fold like objects being lit by a deferred lighting system, emulating a lighting system seen on Eastward

https://user-images.githubusercontent.com/29017432/184543668-893c5b6c-a754-4dc0-b502-7ff17cbf1a63.mov

## Libraries used

- [Dear ImGui for debug UI](https://github.com/ocornut/imgui)
- [GLFW for window context creation](https://github.com/glfw/glfw)
- [glm for Vector maths](https://github.com/g-truc/glm)
- [Glad for OpenGL](https://glad.dav1d.de/)
- [stb_image.h for Image loading](https://github.com/nothings/stb/blob/master/stb_image.h)
- [spdlog for debug logging](https://github.com/gabime/spdlog)
- [SoLoud for Audio](https://github.com/jarikomppa/soloud)
- [Assimp for 3D model importing](https://github.com/assimp/assimp)
- [zlib for data compression](https://zlib.net)
- [libzip for asset archives](https://libzip.org)
- [LUA for scripting](http://www.lua.org/home.html)
- [Sol2 for simplifying lua wrapping process](https://github.com/ThePhD/sol2)
- [Entt for ECS](https://github.com/skypjack/entt)
- [yaml-cpp for Scene and Config file serialization](https://github.com/jbeder/yaml-cpp)
- [json for Asset indexing](https://github.com/nlohmann/json)
- [asio for networking](https://think-async.com/Asio/)
- [OpenSSL for security](https://www.openssl.org)
