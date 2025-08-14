-- Define o ROOT como o diretório onde o script premake5.lua está localizado
local ROOT = _SCRIPT_DIR or "." -- Se _SCRIPT_DIR não estiver definido, usa o diretório atual

package.path = table.concat({
    package.path,
    ROOT .. "/vendor/?.lua",
    ROOT .. "/Rosewood/vendor/?.lua"
}, ";")

-- Criação do Workspace (definir isso no início)
workspace "RosewoodWorkspace"                 -- Nome do seu workspace
configurations { "Debug", "Release", "Dist" } -- Configurações de build
architecture "x86_64"                         -- Arquitetura (se for 32-bit, mude para "x86")

-- Define a variável outputdir
outputdir = "%{cfg.buildcfg}-%{cfg.system}-%{cfg.architecture}"

-- Caminhos para dependências
IncludeDir = {}

IncludeDir["assimp"] = ROOT .. "/Rosewood/vendor/assimp/include"
IncludeDir["GLFW"] = "/usr/include"
IncludeDir["spdlog"] = ROOT .. "/Rosewood/vendor/spdlog/include"
IncludeDir["Glad"] = ROOT .. "/Rosewood/vendor/Glad/include"
IncludeDir["ImGui"] = ROOT .. "/Rosewood/vendor/imgui"
IncludeDir["glm"] = ROOT .. "/Rosewood/vendor/glm"
IncludeDir["stb_image"] = ROOT .. "/Rosewood/vendor/stb_image/include"
IncludeDir["SoLoud"] = ROOT .. "/Rosewood/vendor/soloud/include"
IncludeDir["zlib"] = ROOT .. "/Rosewood/vendor/zlib"
IncludeDir["libzip"] = ROOT .. "/Rosewood/vendor/libzip"
IncludeDir["entt"] = ROOT .. "/Rosewood/vendor/entt/include"
IncludeDir["lua"] = ROOT .. "/Rosewood/vendor/lua/src"
IncludeDir["sol"] = ROOT .. "/Rosewood/vendor/sol"
IncludeDir["asio"] = ROOT .. "/Rosewood/vendor/asio/include"
IncludeDir["yaml_cpp"] = ROOT .. "/Rosewood/vendor/yaml-cpp/include" -- Caminho correto
IncludeDir["json"] = ROOT .. "/Rosewood/vendor/json/include"
IncludeDir["openssl"] = ROOT .. "/Rosewood/vendor/openssl/include"

-- Verificando se o diretório 'yaml-cpp' existe
local yaml_cpp_path = ROOT .. "/Rosewood/vendor/yaml-cpp"
local yaml_cpp_found = os.isdir(yaml_cpp_path)

if not yaml_cpp_found then
    print("Erro: Não foi encontrado o diretório 'yaml-cpp' no caminho esperado: " .. yaml_cpp_path)
    os.exit(1) -- Termina a execução do Premake se o diretório não for encontrado
end

-- Atualizando para usar 'externalincludedirs' no lugar de 'sysincludedirs'
filter "system:linux"
externalincludedirs { IncludeDir["assimp"], IncludeDir["GLFW"], IncludeDir["spdlog"], IncludeDir["Glad"], IncludeDir["ImGui"], IncludeDir["glm"], IncludeDir["stb_image"], IncludeDir["SoLoud"], IncludeDir["zlib"], IncludeDir["libzip"], IncludeDir["entt"], IncludeDir["lua"], IncludeDir["sol"], IncludeDir["asio"], IncludeDir["yaml_cpp"], IncludeDir["json"], IncludeDir["openssl"] }
filter {}

-- Compatibilidade com versões antigas do Premake (shim para 'configuration')
if type(configuration) ~= "function" then
    function configuration(expr)
        if expr == nil then
            filter({})
        elseif type(expr) == "string" then
            filter(expr)
        elseif type(expr) == "table" then
            filter(expr)
        else
            filter(expr)
        end
    end
end

-- Include para dependências
group "Dependencies"
include(ROOT .. "/Rosewood/vendor/soloud/build")
include(ROOT .. "/Rosewood/vendor/Glad")
include(ROOT .. "/Rosewood/vendor/imgui")
include(ROOT .. "/Rosewood/vendor/assimp")
include(ROOT .. "/Rosewood/vendor/zlib")
include(ROOT .. "/Rosewood/vendor/libzip")
include(ROOT .. "/Rosewood/vendor/lua")
-- Não tentamos mais incluir o arquivo premake5.lua do yaml-cpp
group ""

-- Projetos dentro do Workspace
include(ROOT)
include "TestGame"
include "Game/Server"
include "Game/Client"
