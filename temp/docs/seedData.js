const EnumerationType = [
    {
        enumTypeId: "gender",
        description: "جنسیت",
    },{
        enumTypeId: "namePrefix",
        description: "پیشوند",
    },{
        enumTypeId: "assetType",
        description: "نوع دارایی",
    },{
        enumTypeId: "buildingType",
        description: "نوع ساختمان",
    },{
        enumTypeId: "moduleType",
        description: "نوع ماژول",
    },{
        enumTypeId: "vehicleType",
        description: "نوع وسیله نقلیه",
    },{
        enumTypeId: "stockCategory",
        description: "دسته کالا",
    },{
        enumTypeId: "taskCategory",
        description: "دسته کار",
    },{
        enumTypeId: "taskStatus",
        description: "وضعیت کار",
    },{
        enumTypeId: "taskPriority",
        description: "اولویت کار",
    },{
        enumTypeId: "buildingStatus",
        description: "وضعیت انبار",
    },{
        enumTypeId: "vehicleStatus",
        description: "وضعیت وسیله نقلیه",
    },{
        enumTypeId: "moduleStatus",
        description: "وضعیت ماژول",
    }
]

const Enumeration = [
    {
        enumId: "genMale",
        description: "مرد",
        enumTypeId: "gender",
    },{
        enumId: "genFemale",
        description: "زن",
        enumTypeId: "gender",
    },{
        enumId: "preDr",
        description: "دکتر",
        enumTypeId: "namePrefix",
    },{
        enumId: "preEng",
        description: "مهندس",
        enumTypeId: "namePrefix",
    },{
        enumId: "preMr",
        description: "آقا",
        enumTypeId: "namePrefix",
    },{
        enumId: "preMs",
        description: "خانم",
        enumTypeId: "namePrefix",
    },{
        enumId: "astPerson",
        description: "پرسنل",
        enumTypeId: "assetType",
    },{
        enumId: "astVehicle",
        description: "وسیله نقلیه",
        enumTypeId: "assetType",
    },{
        enumId: "modAnchor",
        description: "",
        enumTypeId: "moduleType",
    },{
        enumId: "modTag",
        description: "",
        enumTypeId: "moduleType",
    },{
        enumId: "vhcForklift",
        description: "لیفتراک",
        enumTypeId: "vehicleType",
    },{
        enumId: "bldWarehouse",
        description: "انبار",
        enumTypeId: "buildingType",
    },{
        enumId: "tskCatCargoHandling",
        description: "جابجایی بار",
        enumTypeId: "taskCategory",
    },{
        enumId: "tskStaOpen",
        description: "باز",
        enumTypeId: "taskStatus",
    },{
        enumId: "tskStaInProgress",
        description: "در حال انجام",
        enumTypeId: "taskStatus",
    },{
        enumId: "tskStaDone",
        description: "تکمیل",
        enumTypeId: "taskStatus",
    },{
        enumId: "tskStaWaitingForLoading",
        description: "در انتظار بارگیری",
        enumTypeId: "taskStatus",
    },{
        enumId: "tskStaLoaded",
        description: "بارگیری شده",
        enumTypeId: "taskStatus",
    },{
        enumId: "tskStaMoved",
        description: "منتقل شده",
        enumTypeId: "taskStatus",
    },{
        enumId: "bldStaActive",
        description: "فعال",
        enumTypeId: "buildingStatus",
    },{
        enumId: "bldStaClosed",
        description: "تعطیل",
        enumTypeId: "buildingStatus",
    },{
        enumId: "bldStaUnderRepair",
        description: "در حال تعمیرات",
        enumTypeId: "buildingStatus",
    },{
        enumId: "bldStaSold",
        description: "فروخته شده",
        enumTypeId: "buildingStatus",
    },{
        enumId: "vhcStaActive",
        description: "فعال",
        enumTypeId: "vehicleStatus",
    },{
        enumId: "vhcStaDown",
        description: "از کار افتاده",
        enumTypeId: "vehicleStatus",
    },{
        enumId: "vhcStaUnderRepair",
        description: "در حال تعمیر",
        enumTypeId: "vehicleStatus",
    },{
        enumId: "vhcStaSold",
        description: "فروخته شده",
        enumTypeId: "vehicleStatus",
    },{
        enumId: "modStaActive",
        description: "فعال",
        enumTypeId: "moduleStatus",
    },{
        enumId: "modStaDown",
        description: "خراب",
        enumTypeId: "moduleStatus",
    },{
        enumId: "modStaUnderRepair",
        description: "در حال تعمیر",
        enumTypeId: "moduleStatus",
    },{
        enumId: "modStaNotInstalled",
        description: "نصب نشده",
        enumTypeId: "moduleStatus",
    }
]