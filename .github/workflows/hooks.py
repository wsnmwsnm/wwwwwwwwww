from pythonforandroid.toolchain import Recipe, current_directory, shprint, info
from os.path import exists, join
import sh
import os

class AssetsHook(Recipe):
    name = 'assets'
    depends = []
    
    def prebuild_arch(self, arch):
        super().prebuild_arch(arch)
        
        assets_dir = join(self.ctx.root_dir, 'assets')
        if exists(assets_dir):
            target_dir = join(self.ctx.get_python_install_dir(), 'assets')
            if not exists(target_dir):
                os.makedirs(target_dir)
            
            for file_name in ['a', 'b', 'c', 'd', 'e', 'icon.png']:
                src = join(assets_dir, file_name)
                if exists(src):
                    shprint(sh.cp, src, target_dir)
                    info(f"Copied {file_name} to assets")

assets_hook = AssetsHook()