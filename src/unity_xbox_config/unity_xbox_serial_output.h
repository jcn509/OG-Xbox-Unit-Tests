#include "windows.h"
#define UNITY_OUTPUT_CHAR(a)  \
    {                         \
        char x[] = " ";       \
        x[0] = (char)a;       \
        OutputDebugString(x); \
    }
#define UNITY_OUTPUT_START() \
    {                        \
    }
#define UNITY_OUTPUT_FLUSH() \
    {                        \
    }
#define UNITY_OUTPUT_COMPLETE() \
    {                           \
    }