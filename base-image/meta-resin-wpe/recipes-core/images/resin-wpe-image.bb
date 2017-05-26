include recipes-core/images/core-image-minimal.bb

IMAGE_FSTYPES = "tar.gz"

DISTRO_FEATURES_remove = "wayland"

IMAGE_INSTALL_append += " \
	fbcp \
	fontconfig \
	fontconfig-utils \
	tslib-calibrate \
	tslib-tests \
	ttf-bitstream-vera \
	wpebackend \
	wpebackend-rdk \
	wpelauncher \
	wpewebkit \
	python3 \
	python3-dev \
	python3-modules \
	python3-pip \
	packagegroup-core-buildessential \
	cmake \
	curl \
	unzip \
	swig \
	git \
	libudev \
	eudev-dev \
	libxrandr \
	libxrandr-dev \
	userland-dev \
	"

VIRTUAL-RUNTIME_init_manager="busybox"
