const fs = require('fs-extra');
const path = require('path');
const { execSync } = require("child_process");
const rimraf = require('rimraf');

const rpath = 'C:\\Users\\ueqt\\safaribooks\\Downloads\\';
const tpath = 'C:\\Users\\ueqt\\OneDrive - ueqt\\safaribooks\\';
// const rpath = 'E:\\Downloads\\';
const zip = 'c:\\Program Files\\7-Zip\\7z.exe';

const dozip = async () => {
    const files = fs.readdirSync(rpath);
    for (let i = 0; i < files.length; i++) {
        if(files[i] === '_index') {
            continue;
        }

        const cpath = path.join(rpath, files[i]);
        console.log(cpath);

        if (!fs.statSync(cpath).isDirectory()) {
            // 文件直接跳过
            continue;
        }

        if(!fs.existsSync(path.join(cpath, files[i] + '.epub'))) {
            // 还在下载中
            continue;
        }

        // 先删除原来的epub文件
        rimraf.sync(path.join(cpath, files[i] + '.epub'));

        // 压缩
        execSync(`"${zip}" a "${files[i]}.epub" "${cpath}\\*"`, {
            cwd: rpath,
            stdio: 'inherit'
        });
        rimraf.sync(cpath);
        // 先删除原来的epub文件
        rimraf.sync(path.join(tpath, files[i] + '.epub'));
        try
        {
        fs.moveSync(path.join(rpath, files[i] + '.epub'), path.join(tpath, files[i] + '.epub'));
        }
        catch
        {
            rimraf.sync(path.join(rpath, files[i] + '.epub'));
        }
    }
}

const main = async () => {
    await dozip();
}
main();