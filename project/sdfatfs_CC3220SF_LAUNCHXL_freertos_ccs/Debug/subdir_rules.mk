################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Each subdirectory must supply rules for building sources it contributes
CC3220SF_LAUNCHXL.obj: ../CC3220SF_LAUNCHXL.c $(GEN_OPTS) | $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"/Applications/ti/ccsv7/tools/compiler/ti-cgt-arm_16.9.1.LTS/bin/armcl" -mv7M4 --code_state=16 --float_support=vfplib -me --include_path="/Users/colton/workspace_v72/sdfatfs_CC3220SF_LAUNCHXL_freertos_ccs" --include_path="/Users/colton/ti/simplelink_cc32xx_sdk_1_30_01_03/source" --include_path="/Users/colton/ti/simplelink_cc32xx_sdk_1_30_01_03/kernel/freertos/posix" --include_path="/FreeRTOS/Source/include" --include_path="/FreeRTOS/Source/portable/CCS/ARM_CM3" --include_path="/Users/colton/workspace_v72/freertos_builds_CC3220SF_LAUNCHXL_release_ccs" --include_path="/Applications/ti/ccsv7/tools/compiler/ti-cgt-arm_16.9.1.LTS/include" -g --diag_warning=225 --diag_warning=255 --diag_wrap=off --display_error_number --gen_func_subsections=on --preproc_with_compile --preproc_dependency="CC3220SF_LAUNCHXL.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

fatsd.obj: ../fatsd.c $(GEN_OPTS) | $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"/Applications/ti/ccsv7/tools/compiler/ti-cgt-arm_16.9.1.LTS/bin/armcl" -mv7M4 --code_state=16 --float_support=vfplib -me --include_path="/Users/colton/workspace_v72/sdfatfs_CC3220SF_LAUNCHXL_freertos_ccs" --include_path="/Users/colton/ti/simplelink_cc32xx_sdk_1_30_01_03/source" --include_path="/Users/colton/ti/simplelink_cc32xx_sdk_1_30_01_03/kernel/freertos/posix" --include_path="/FreeRTOS/Source/include" --include_path="/FreeRTOS/Source/portable/CCS/ARM_CM3" --include_path="/Users/colton/workspace_v72/freertos_builds_CC3220SF_LAUNCHXL_release_ccs" --include_path="/Applications/ti/ccsv7/tools/compiler/ti-cgt-arm_16.9.1.LTS/include" -g --diag_warning=225 --diag_warning=255 --diag_wrap=off --display_error_number --gen_func_subsections=on --preproc_with_compile --preproc_dependency="fatsd.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

main_freertos.obj: ../main_freertos.c $(GEN_OPTS) | $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"/Applications/ti/ccsv7/tools/compiler/ti-cgt-arm_16.9.1.LTS/bin/armcl" -mv7M4 --code_state=16 --float_support=vfplib -me --include_path="/Users/colton/workspace_v72/sdfatfs_CC3220SF_LAUNCHXL_freertos_ccs" --include_path="/Users/colton/ti/simplelink_cc32xx_sdk_1_30_01_03/source" --include_path="/Users/colton/ti/simplelink_cc32xx_sdk_1_30_01_03/kernel/freertos/posix" --include_path="/FreeRTOS/Source/include" --include_path="/FreeRTOS/Source/portable/CCS/ARM_CM3" --include_path="/Users/colton/workspace_v72/freertos_builds_CC3220SF_LAUNCHXL_release_ccs" --include_path="/Applications/ti/ccsv7/tools/compiler/ti-cgt-arm_16.9.1.LTS/include" -g --diag_warning=225 --diag_warning=255 --diag_wrap=off --display_error_number --gen_func_subsections=on --preproc_with_compile --preproc_dependency="main_freertos.d" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '


