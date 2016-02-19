'''List of Locally installed Modules'''

import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

'''Path of a module'''

import pvlib
print pvlib.__file__

'''What a module contains'''

import pvlib
print dir(pvlib)