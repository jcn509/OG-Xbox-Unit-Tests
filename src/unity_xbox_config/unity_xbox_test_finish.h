
#include "windows.h"

extern int UnityEnd();

static int UnityEndXbox()
{
    int ret = UnityEnd();
    OutputDebugString("Xbox Unity tests are complete!\n");
    while (1)
    {
    }
    return ret;
}

#define UNITY_END() UnityEndXbox()
