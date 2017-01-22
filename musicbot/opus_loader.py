from discord import opus

# [MBM] Multi-Language support
# required for language support
from musicbot.config import Config, ConfigDefaults
import importlib
# ===== END =====

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass
# [MBM] Multi-Language support
        self.config = Config(config_file)
        language = self.config.language
        f = self.config.languages_location + language
        self.lang = importlib.import_module(f)
# ===== END =====
    raise RuntimeError(self.lang.opus_error_loading % (', '.join(opus_libs)))
