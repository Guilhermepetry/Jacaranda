# Jacarandá

**Jacarandá** is a personal fork of the [Rosewood Game Engine](https://github.com/dovker/Rosewood), originally created by Dovydas Vaičiukynas.  
The purpose of this fork is purely educational — mainly to study the *Deferred pseudo-3D rendering* example, which emulates a lighting system similar to the one used in the game [Eastward](https://www.indiedb.com/games/eastward/images/lighting-test).

I recently started studying computer graphics and I am a complete beginner in the field. This project serves as a playground for experimentation and learning.

The name **Jacarandá** is the Portuguese translation of *Rosewood*.

---

## Rosewood
Rosewood Game Engine

**Rosewood Engine** is a game engine created for me to learn Graphics Programming and to learn how Game Engines work

## Plan
!! THIS GAME ENGINE IS NO LONGER BEING DEVELOPED OR SUPPORTED !!
My plan for this engine is to develop it to a point I can make an advanced 2D game and a simple 3D game with it, whilst learning Game Engine development, Design patterns, graphics programming, Advanced c++, problem solving.

## Features
* OpenGL Support
* Cross-Platform (Tested on major desktop platforms)
* 2D Rendering
* Asset managment system
* 2D Audio support
* ECS
* File system and Compression
* Lua Scripting
* Basic Networking


## Screenshots

### Lua Scripting demonstration
All the characters seen on this demonstration are being controled via a Lua Script

https://user-images.githubusercontent.com/29017432/184543662-437f4487-839a-4301-a8f8-e27e1b23cb56.mov

### Deferred pseudo-3D rendering
What you're seeing here is an orthographic projection of 3D paper-fold like objects being lit by a deferred lighting system, emulating a lighting system seen on Eastward

https://user-images.githubusercontent.com/29017432/184543668-893c5b6c-a754-4dc0-b502-7ff17cbf1a63.mov



## Building
## All Platforms
  1. If you try to make project and it fails, make sure every dependency has it's premake5.lua file, if not, you can find those files in **"vendor/premakes"** folder.
  2. **IMPORTANT!** Make sure to compile OpenSSL in the **"Rosewood/vendor/openssl"** directory as a Static Library (Using **"no-shared"** option).
  3. Open the **Build Tool**, located in **"Tools/BuildTool.py"**
## Windows:
  1. Generate project files by selecting the project and generator type.
  2. Open in preferred IDE or Open **Build Tool** and press the **Build** and **Run** buttons if you chose `gmake2`
  
## MacOS:
  1. Download Premake5 binaries for Mac OS and paste them in **"vendor/bin/premake"** folder.
  2. Use the **Build Tool** to create `MakeFiles` or `XCode` files
  3. Press **Build** and **Run** if you chose `MakeFiles` or open your `XCode` files and build there.

## Linux:
  1. Download Premake5 binaries for Linux and paste them in **"vendor/bin/premake"** folder.
  2. REQUIRED PACKAGES:
    * `xorg-dev`
    * `libasound2-dev`
  3. Open **Build Tool** and create `MakeFiles`
  4. Press **Build** and **Run**
### **[Trello board](https://trello.com/b/bTRVKkrL/rosewood-engine)**

## Libraries used
* [Dear ImGui for debug UI](https://github.com/ocornut/imgui)
* [GLFW for window context creation](https://github.com/glfw/glfw)
* [glm for Vector maths](https://github.com/g-truc/glm)
* [Glad for OpenGL](https://glad.dav1d.de/)
* [stb_image.h for Image loading](https://github.com/nothings/stb/blob/master/stb_image.h)
* [spdlog for debug logging](https://github.com/gabime/spdlog)
* [SoLoud for Audio](https://github.com/jarikomppa/soloud)
* [Assimp for 3D model importing](https://github.com/assimp/assimp)
* [zlib for data compression](https://zlib.net)
* [libzip for asset archives](https://libzip.org)
* [LUA for scripting](http://www.lua.org/home.html)
* [Sol2 for simplifying lua wrapping process](https://github.com/ThePhD/sol2)
* [Entt for ECS](https://github.com/skypjack/entt)
* [yaml-cpp for Scene and Config file serialization](https://github.com/jbeder/yaml-cpp)
* [json for Asset indexing](https://github.com/nlohmann/json)
* [asio for networking](https://think-async.com/Asio/)
* [OpenSSL for security](https://www.openssl.org)
