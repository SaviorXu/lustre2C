#include "test123_interface.h"
#include "test123_type.h"
#include "test123_mapping.h"
#include "SmuVTable.h"
#include <string.h>

#define UNUSED(x) (void)(x)
/* context */

inC_lustre_pre_lustre_time inputs_ctx;
static inC_lustre_pre_lustre_time inputs_ctx_execute;
outC_lustre_pre_lustre_time outputs_ctx;

static void _SCSIM_RestoreInterface(void) {
    init_kcg_int8(&inputs_ctx.in_X);
    init_kcg_int8(&inputs_ctx_execute.in_X);
    memset((void*)&outputs_ctx, 0, sizeof(outputs_ctx));
}

static void _SCSIM_ExecuteInterface(void) {
    pSimulator->m_pfnAcquireValueMutex(pSimulator);
    inputs_ctx_execute.in_X = inputs_ctx.in_X;
    pSimulator->m_pfnReleaseValueMutex(pSimulator);
}

#ifdef __cplusplus
extern "C" {
#endif

const int  rt_version = Srtv62;

const char* _SCSIM_CheckSum = "";
const char* _SCSIM_SmuTypesCheckSum = "6757860ac1d8ce9bd3fc91d925ceefb8";

/* simulation */

int SimInit(void) {
    int nRet = 0;
    _SCSIM_RestoreInterface();
#ifdef EXTENDED_SIM
    BeforeSimInit();
#endif
#ifndef KCG_USER_DEFINED_INIT
    lustre_pre_init_lustre_time(&outputs_ctx);
    nRet = 1;
#else
    nRet = 0;
#endif
#ifdef EXTENDED_SIM
    AfterSimInit();
#endif
    return nRet;
}

int SimReset(void) {
    int nRet = 0;
    _SCSIM_RestoreInterface();
#ifdef EXTENDED_SIM
    BeforeSimInit();
#endif
#ifndef KCG_NO_EXTERN_CALL_TO_RESET
    lustre_pre_reset_lustre_time(&outputs_ctx);
    nRet = 1;
#else
    nRet = 0;
#endif
#ifdef EXTENDED_SIM
    AfterSimInit();
#endif
    return nRet;
}

#ifdef __cplusplus
    #ifdef pSimoutC_lustre_pre_lustre_timeCIVTable_defined
        extern struct SimCustomInitVTable *pSimoutC_lustre_pre_lustre_timeCIVTable;
    #else 
        struct SimCustomInitVTable *pSimoutC_lustre_pre_lustre_timeCIVTable = NULL;
    #endif
#else
    struct SimCustomInitVTable *pSimoutC_lustre_pre_lustre_timeCIVTable;
#endif

int SimCustomInit(void) {
    int nRet = 0;
    if (pSimoutC_lustre_pre_lustre_timeCIVTable != NULL && 
        pSimoutC_lustre_pre_lustre_timeCIVTable->m_pfnCustomInit != NULL) {
        /* VTable function provided => call it */
        nRet = pSimoutC_lustre_pre_lustre_timeCIVTable->m_pfnCustomInit ((void*)&outputs_ctx);
    }
    else {
        /* VTable misssing => error */
        nRet = 0;
    }
    return nRet;
}

#ifdef EXTENDED_SIM
    int GraphicalInputsConnected = 1;
#endif

int SimStep(void) {
#ifdef EXTENDED_SIM
    if (GraphicalInputsConnected)
        BeforeSimStep();
#endif
    _SCSIM_ExecuteInterface();
    lustre_pre_lustre_time(&inputs_ctx_execute, &outputs_ctx);
#ifdef EXTENDED_SIM
    AfterSimStep();
#endif
    return 1;
}

int SimStop(void) {
#ifdef EXTENDED_SIM
    ExtendedSimStop();
#endif
    return 1;
}

void SsmUpdateValues(void) {
#ifdef EXTENDED_SIM
    UpdateValues();
#endif
}

void SsmConnectExternalInputs(int bConnect) {
#ifdef EXTENDED_SIM
    GraphicalInputsConnected = bConnect;
#else
    UNUSED(bConnect);
#endif
}

/* dump */

int SsmGetDumpSize(void) {
    int nSize = 0;
    nSize += sizeof(inC_lustre_pre_lustre_time);
    nSize += sizeof(outC_lustre_pre_lustre_time);
#ifdef EXTENDED_SIM
    nSize += ExtendedGetDumpSize();
#endif
    return nSize;
}

void SsmGatherDumpData(char * pData) {
    char* pCurrent = pData;
    memcpy(pCurrent, &inputs_ctx, sizeof(inC_lustre_pre_lustre_time));
    pCurrent += sizeof(inC_lustre_pre_lustre_time);
    memcpy(pCurrent, &outputs_ctx, sizeof(outC_lustre_pre_lustre_time));
    pCurrent += sizeof(outC_lustre_pre_lustre_time);
#ifdef EXTENDED_SIM
    ExtendedGatherDumpData(pCurrent);
#endif
}

void SsmRestoreDumpData(const char * pData) {
    const char* pCurrent = pData;
    memcpy(&inputs_ctx, pCurrent, sizeof(inC_lustre_pre_lustre_time));
    pCurrent += sizeof(inC_lustre_pre_lustre_time);
    memcpy(&outputs_ctx, pCurrent, sizeof(outC_lustre_pre_lustre_time));
    pCurrent += sizeof(outC_lustre_pre_lustre_time);
#ifdef EXTENDED_SIM
    ExtendedRestoreDumpData(pCurrent);
#endif
}

/* snapshot */

int SsmSaveSnapshot(const char * szFilePath, size_t nCycle) {
    /* Test Services API not available */
    UNUSED(szFilePath);
    UNUSED(nCycle);
    return 0;
}

int SsmLoadSnapshot(const char * szFilePath, size_t *nCycle) {
    /* Test Services API not available */
    UNUSED(szFilePath);
    UNUSED(nCycle);
    return 0;
}

/* checksum */

const char * SsmGetCheckSum() {
    return _SCSIM_CheckSum;
}

const char * SsmGetSmuTypesCheckSum() {
    return _SCSIM_SmuTypesCheckSum;
}

#ifdef __cplusplus
} /* "C" */
#endif

