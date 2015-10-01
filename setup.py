from setuptools import setup

setup(name='tsviewer',
      version='0.1.0',
      description='A GUI for visualizing time series data',
      long_description=('Visualing time series data (such as temperature,'
                        ' humidity, weight, height, etc) is a common task in'
                        ' many projects. This is a lightweight viewer based'
                        ' on the python packages traits, traitsui, and chaco.'
                        ' The user can choose which variables are plotted on'
                        ' the x- and y-axes while a slider moves a tracer'
                        ' point along the data.'),
      classifiers=[  # Classifier list:  https://pypi.python.org/pypi?:action=list_classifiers
                   "Development Status :: 3 - Alpha",
                   "Environment :: X11 Applications",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2 :: Only",
                   "Programming Language :: Python :: 2.7",
                   "Topic :: Scientific/Engineering",
                   "Topic :: Scientific/Engineering :: Information Analysis",
                   "Topic :: Scientific/Engineering :: Visualization",
                   "Topic :: Utilities",
                  ],
      url='https://github.com/sswan/tsviewer',
      author='Scot Swan, Tim Fuller',
      author_email='scot.swan@gmail.com, timothy.fuller@utah.edu',
      license='MIT',
      packages=['tsviewer',],
      package_data={
                    'tsviewer':[
                                'icon/*.png',
                               ]
                   },
      data_files=[
                  'tsviewer/icon/graph.png',
                  'tsviewer/icon/legend.png',
                  'tsviewer/icon/file.png',
                  'tsviewer/icon/hidden.png',
                  'tsviewer/icon/camera.png',
                  'tsviewer/icon/random.png',
                  'tsviewer/icon/plot-scale.png',
                  'tsviewer/icon/frame-first.png',
                  'tsviewer/icon/frame-last.png',
                  'tsviewer/icon/frame-next.png',
                  'tsviewer/icon/frame-previous.png',
                 ],
      entry_points={
                    'console_scripts': ['tsviewer=tsviewer.__main__:main'],
                   },
      install_requires=['numpy', 'traits', 'traitsui', 'chaco', 'pyface',
                        'tabfileio'],
      zip_safe=False)
