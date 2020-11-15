XBE_TITLE = OGXboxUnitTestsExample
GEN_XISO = ${XBE_TITLE}.iso

UNITYDIR = $(CURDIR)/external/Unity/src
SRCDIR = $(CURDIR)/src

SRCS +=	$(SRCDIR)/main.c $(UNITYDIR)/unity.c

# Defining DUNITY_INCLUDE_CONFIG_H Very important if we want to output to the
# serial port!
CFLAGS += -I$(UNITYDIR) -I$(SRCDIR) -DUNITY_INCLUDE_CONFIG_H -DUNITY_DIFFERENTIATE_FINAL_FAIL

NXDK_DIR ?= $(CURDIR)/../nxdk

include $(NXDK_DIR)/Makefile
