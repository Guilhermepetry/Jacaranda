from dearpygui.dearpygui import *
from dearpygui.demo import show_demo
import subprocess
import os
from CustomLogger import *
from PlatformInfo import *
from pathlib import Path
from threading import Thread

# Initialize context first
create_context()

Configurations = ["debug", "release", "dist"]
Applications = ["TestGame", "GameClient", "GameServer", "Sandbox2D", "Sandbox3D"]
PremakeConfigs = ["gmake2", "vs2019", "xcode4"]

# Use tag instead of id
AppComboID = generate_uuid()
WindowID = generate_uuid()
ConfigComboID = generate_uuid()
PremakeComboID = generate_uuid()
GroupID = generate_uuid()

logger = None

SubProcessList = {}
SubProcessUI = {}

def get_workspace_path():
    return str(Path(Path(__file__).parent).parent)

def del_subprocess(index, killBool):
    if(index in SubProcessList):
        if killBool: SubProcessList[index][0].terminate()
        SubProcessList.pop(index)
        # Delete the single container group if it still exists
        row = SubProcessUI.get(index)
        if row is not None:
            if does_item_exist(row):
                delete_item(row)
            SubProcessUI.pop(index, None)

def add_subprocess(index):
    # Create a single container for this row so we only delete one item later
    with group(parent=GroupID) as row_group:
        id_text = add_text('[' + str(SubProcessList[index][0].pid) + '] ' + str(SubProcessList[index][1]))
        with group(horizontal=True):
            add_button(label="Terminate", callback=lambda: del_subprocess(index, True))
        add_separator()
    SubProcessUI[index] = row_group

def process_callback(process, command):
    while True:
        output = process.stdout.readline()
        if output != "": logger.log(output.strip())

        return_code = process.poll()
        if return_code is not None:
            logger.log_tool("----------------")
            logger.log_tool("Finished calling " + command[0])
            logger.log_tool("----------------")
            del_subprocess(process.pid, False)
            break

def call_command(workspace, command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True, cwd=workspace, stderr=subprocess.STDOUT)
    SubProcessList[process.pid] = [process, command]
    add_subprocess(process.pid)
    thread = Thread(target=process_callback, args=[process, command])
    thread.start()

def build_callback(sender, app_data):
    call_command(get_workspace_path(), ['make', 'config=' + get_value(ConfigComboID)])

def premake_callback(sender, app_data):
    call_command(get_workspace_path(), [get_call_thing() + os.path.join("vendor", "bin", "premake", "premake5") + get_executable_ext(), get_value(PremakeComboID)])

def run_callback(sender, app_data):
    exe_path = os.path.join(get_workspace_path(), 'bin', 
                            get_value(ConfigComboID).capitalize() + '-' + get_platform() + "-x86_64", 
                            get_value(AppComboID))
    exe_file = exe_path + get_executable_ext()
    
    # Check if directory and executable exist
    if not os.path.exists(exe_path):
        if logger:
            logger.log_error(f"Directory not found: {exe_path}")
            logger.log_error("Please build the project first!")
        return
    
    if not os.path.exists(exe_file):
        if logger:
            logger.log_error(f"Executable not found: {exe_file}")
            logger.log_error("Please build the project first!")
        return
    
    # If it exists, run it
    call_command(exe_path, [get_call_thing() + get_value(AppComboID) + get_executable_ext()])

FontScale = 1.2

# Use tag instead of id
with window(label="Rosewood Build Tool", tag=WindowID) as main_window:
    with group(tag=GroupID):
        set_global_font_scale(FontScale)
        add_separator()
        add_text("Build Project")
        add_combo(label="Configurations", tag=ConfigComboID, default_value="debug", items=Configurations, width=200)
        add_combo(label="Project", tag=AppComboID, default_value="TestGame", items=Applications, width=200)
        
        # Use horizontal group instead of add_same_line
        with group(horizontal=True):
            add_button(label="Build", callback=build_callback, width=100, height=40)
            add_button(label="Run", callback=run_callback, width=100, height=40)
        
        add_separator()
        add_text("Generate Project")
        add_combo(label="Project generator type", tag=PremakeComboID, default_value="gmake2", items=PremakeConfigs, width=200)
        add_button(label="Generate project files", callback=premake_callback, width=200, height=40)
        add_separator()
        add_separator()
        add_text("SubProcesses:")
        add_separator()
    
    # Create log group - changed variable name from 'group' to 'log_group'
    with group(horizontal=True):
        log_group = add_group(label="Log")
    logger = Logger(log_group)

set_primary_window(WindowID, True)

# Correct viewport setup
create_viewport(title='Rosewood Build Tool', width=800, height=600)
setup_dearpygui()

show_viewport()
start_dearpygui()
destroy_context()