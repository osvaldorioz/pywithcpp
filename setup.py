from setuptools import setup, Extension
import pybind11

# Definir el módulo de extensión
ext_modules = [
    Extension(
        'bindings',                        # Nombre del módulo
        ['app/bindings.cpp'],               # Archivo fuente C++
        include_dirs=[pybind11.get_include()],  # Incluir encabezados de Pybind11
        language='c++'
    )
]

# Configuración del paquete
setup(
    name='bindings',
    version='0.1',
    ext_modules=ext_modules,
    install_requires=['pybind11'],
    zip_safe=False,
)
