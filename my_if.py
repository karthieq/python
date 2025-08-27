# Comparisons:
#  Equal:            ==
#  Not Equal:        !=
#  Greater Than:     >
#  Less Than:        <
#  Greater or Equal: >=
#  Less or Equal:    <=
#  Object Identity:  is

# Logical Operators:
#  and
#  or
#  not

# False Values:
#  False
#  None
#  Zero of any numeric type
#  Any empty sequence. For example, '', (), []
#  Any empty mapping. For example, {}

condition = 0.0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


string = """Oracle Enterprise Manager 24ai Release 1
Copyright (c) 1996, 2024 Oracle Corporation.  All rights reserved.
Console Server Host        : systemtest-14612-oms0-0-248306.subnet1rg2phxsu.emdevinfraphx1.oraclevcn.com
HTTP Console Port          : 7788
HTTPS Console Port         : 7799
HTTP Upload Port           : 4889
HTTPS Upload Port          : 4903
EM Instance Home           : /scratch/kramanuj/24c/241114/gc_inst/em/EMGC_OMS1
OMS Log Directory Location : /scratch/kramanuj/24c/241114/gc_inst/em/EMGC_OMS1/sysman/log
SLB or virtual hostname: 144.25.120.106
HTTPS SLB Upload Port : 4903
HTTPS SLB Console Port : 443
HTTPS SLB JVMD Port : 7301
Agent Upload is unlocked.
OMS Console is unlocked.
Active CA ID: 1
Console URL: https://144.25.120.106:443/em
Upload URL: https://144.25.120.106:4903/empbs/upload

WLS Domain Information
Domain Name            : EMGC_DOMAIN
Admin Server Host      : systemtest-14612-oms0-0-248306.subnet1rg2phxsu.emdevinfraphx1.oraclevcn.com
Admin Server HTTPS Port: 7101
Admin Server is RUNNING

Extended Domain Name            : EMExtDomain1
Extended Admin Server Host      : systemtest-14612-oms0-0-248306.subnet1rg2phxsu.emdevinfraphx1.oraclevcn.com
Extended Admin Server HTTPS Port: 7002
Extended Admin Server is RUNNING

Oracle Management Server Information
Managed Server Instance Name: EMGC_OMS1
Oracle Management Server Instance Host: systemtest-14612-oms0-0-248306.subnet1rg2phxsu.emdevinfraphx1.oraclevcn.com
WebTier is Up
Oracle Management Server is Up
JVMD Engine is Up"""

if any(em_ver in string for em_ver in [" 24 ", " 24ai "]):
    print('found')
