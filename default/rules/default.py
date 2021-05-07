from src.base import Target

Target(
    name = 'default',
    package = True,
    dependencies = [
        'yosys',
        'nextpnr-generic',
        'nextpnr-ice40',
        'nextpnr-ecp5',
        'nextpnr-machxo2',
        'nextpnr-nexus',
        'icestorm',
        'prjtrellis',
        #'prjoxide',
        'dfu-util',
        'ecpprog',
        'openfpgaloader',
        'avy',
        'boolector',
        'yices',
        'suprove',
        'pono',
        'z3',
        'mcy',
        'sby',
        'sby-gui',
        #'ghdl',
        'gtkwave',
        'verilator',
        'iverilog',
        'litex',
        'ecpdap',
        'fujprog',
        'python-programmers',
        'openocd',
        'icesprog',
    ],
    patches = [ 'win-launcher.c' ],
    resources = [ 'system-resources' ],
)
