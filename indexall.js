const fs = require("fs");
const path = require("path");

let sourcePath = '../OneDrive - ueqt/safaribooks/_index'
var files = fs.readdirSync(sourcePath);
let result = {
    datas: {},
    keys: {}
};
for (let i = 0; i < files.length; i++) {
    console.log(`${i + 1} / ${files.length}`);
    if(files[i].lastIndexOf('.json') < 0) {
        continue;
    }
    const cpath = path.join(sourcePath, files[i]);
    let data = {};
    while(true) {
        try {
            data = JSON.parse(fs.readFileSync(cpath, { encoding: 'utf-8'}));
            break;
        } catch(err) {
            console.error(err);
        }
    }
    result.datas[data["archive_id"]] = data;
    Object.keys(data).forEach(key => {
        if(!result.keys[key]) {
            result.keys[key] = [];
        }
        if(!result.keys[key].includes(data[key])) {
            result.keys[key].push(data[key]);
        }
    });
}

if (result) {
    fs.writeFileSync(path.join(sourcePath, '..', 'all.json'), JSON.stringify(result), {encoding: 'utf-8'});
}