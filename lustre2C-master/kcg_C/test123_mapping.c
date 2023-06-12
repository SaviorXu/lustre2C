/* test123_mapping.c */

#include "test123_type.h"
#include "test123_interface.h"
#include "test123_mapping.h"

#include "SmuTypes.h"
#include "SmuMapping.h"

#include "kcg_sensors.h"

/* mapping declaration */

#define DECL_ITER(name) extern const MappingIterator iter_##name


#define DECL_SCOPE(name, count) extern const MappingEntry name##_entries[count]; extern const MappingScope name

DECL_SCOPE(scope_1, 2);
DECL_SCOPE(scope_0, 1);

/* clock definition */


/* mapping definition */


const MappingEntry scope_1_entries[2] = {
    /* 0 */ { MAP_OUTPUT, "out_Y", NULL, sizeof(kcg_int8), (size_t)&outputs_ctx.out_Y, &_Type_kcg_int8_Utils, NULL, NULL, NULL, 1, 0 },
    /* 1 */ { MAP_INPUT, "in_X", NULL, sizeof(kcg_int8), (size_t)&inputs_ctx.in_X, &_Type_kcg_int8_Utils, NULL, NULL, NULL, 1, 1 }
};
const MappingScope scope_1 = {
    "lustre_time::lustre_pre/ lustre_pre_lustre_time",
    scope_1_entries, 2
};

const MappingEntry scope_0_entries[1] = {
    /* 0 */ { MAP_ROOT, "lustre_time::lustre_pre", NULL, 0, 0, NULL, NULL, NULL, &scope_1, 1, 0 }
};
const MappingScope scope_0 = {
    "",
    scope_0_entries, 1
};

/* entry point */
const MappingScope* pTop = &scope_0;
