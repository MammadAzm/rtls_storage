const services = [
{
name: "login",
type: "post",
rest: "/login",
input: `{ 
    username,
    password,
}`,
output: `{ 
    username,
    assetId,
    firstName,
    lastName,
    fullName, //includes firstName, lastName, and suffix
    prefixEnumId,
    prefix, //description of prefixEnumId
    postId,
    postTitle,
    avatar,
    accessToken,
    accessLevels: []
}`,
},

{
name: "logout",
type: "delete",
rest: "/logout",
input: `-`,
output: `-`,
},

{
name: "enums",
type: "get",
rest: "/enums",
input: `-`,
output: `[{
    ...Enumeration, //all Enumeration fields,
}]`,
},

{
name: "tasks",
type: "get",
rest: "/tasks",
description: "returns records of Task which are related to logined user.",
input: `{
    categoryEnumId, //ignore if empty
    statusEnumId, //ignore if empty
    priorityEnumId, //ignore if empty
}`,
output: `[{
    ...Task, //all Task fields,
    category, //description of categoryEnumId
    status, //description of statusEnumId
    priority, //description of priorityEnumId
    progress, //percent of progress based on its subtasks status
    fromDate, //from TaskResponsible
    thruDate, //from TaskResponsible
}]`,
},

{
name: "task",
type: "get",
rest: "/tasks/:taskId",
description: "returns task details.",
input: `{
    taskId
}`,
output: `[{
    ...Task, //all Task fields,
    subtasks: []
}]`,
},

{
name: "loadCargo",
type: "post",
rest: "/tasks/cargoHandling/loadCargo",
description: "changes the task status to 'taskStaLoaded'.",
input: `{
    taskId
}`,
output: `-`,
},

{
name: "moveCargo",
type: "post",
rest: "/tasks/cargoHandling/moveCargo",
description: "changes the task status to 'taskStaMoved'.",
input: `{
    taskId
}`,
output: `-`,
},

{
name: "cargoReception",
type: "post",
rest: "/tasks/cargoHandling/cargoReception",
description: "",
input: `{
    buildingId,
    floorId, //put the first floor (floor with index of zero) of the warehouse 
    fromDate,
    description,
    cargoList: [{
        stockId,
        count,
    }]
}`,
output: `-`,
},

{
name: "personnel",
type: "get",
rest: "/assets/personnel",
input: `-`,
output: `[{
    ...Person, //all Person fields,
    postTitle, //title of postId
    postCode, //code of postId
    gender, //description of genderEnumId
    prefix, //description of prefixEnumId
}]`,
},

{
name: "vehicles",
type: "get",
rest: "/assets/vehicles",
input: `-`,
output: `[{
    ...Vehicle, //all Vehicle fields,
    status, //description of statusEnumId
    type, //description of typeEnumId
}]`,
},

{
name: "buildings",
type: "get",
rest: "/assets/buildings",
input: `-`,
output: `[{
    ...Building, //all Building fields,
    status, //description of statusEnumId
    type, //description of typeEnumId
}]`,
},

{
name: "modules",
type: "get",
rest: "/assets/modules",
input: `-`,
output: `[{
    ...Module, //all Module fields,
    assetName, //name of vehicle or fullName of person with assetId
    type, //description of typeEnumId
}]`,
},

{
name: "warehouses",
type: "get",
rest: "/inventory/warehouses",
description: "returns buildings with 'bldWarehouse' typeEnumId",
input: `-`,
output: `[{
    ...Building, //all Building fields,
}]`,
},

{
name: "warehousesWithReport",
type: "get",
rest: "/inventory/warehousesWithReport",
input: `-`,
output: `[{
    ...Building, //all Building fields,
    capacity, //total warehouse capacity (sum of its floors capacity)
    fullness, //total volume of available pallets  
    status, //description of statusEnumId
    type, //description of typeEnumId
}]`,
},

{
name: "stockes",
type: "get",
rest: "/inventory/stockes",
input: `-`,
output: `[{
    ...Stock, //all Stock fields,
    category, //description of categoryEnumId
}]`,
},
]