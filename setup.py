import setuptools
setuptools.setup(
    name="Real-Time-Voice-Cloning",
    version="0.0.1",
    python_requires='>=3.6',
    install_requires=['tensorflow==1.15', 'torch', 'webrtcvad', 'umap-learn', 'visdom','librosa>=0.5.1','matplotlib>=2.0.2','numpy>=1.14.0' \
                      'scipy>=1.0.0','tqdm','sounddevice', 'SoundFile','Unidecode', 'inflect', 'PyQt5', 'multiprocess','numba==0.48']
)