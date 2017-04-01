# Catpaw's maven-repo

## Gradle Plugins

### apkuploaders
Use to develop apk file to pgyer.

#### Usage
Add dependencies in root project build.gradle file.

```groovy
buildscript {
    repositories {
        jcenter()
        maven {
            url "https://raw.githubusercontent.com/congtaowang/maven-repo/master/"
        }
    }
    dependencies {
        classpath 'com.catpaw:apkuploaders:1.0.0'
    }
}
```

Apply plugin in module project build.gradle

```groovy
apply plugin: 'com.catpaw.plugins.apkuploaders'
```

Config upload paramaters in module project build.gradle file.

```groovy
apkUploaderConfigurator {
    //Your apk archive file directory.
    archiveDirectory = file(new File(buildDir.path, "archives"))

    pgyer {
        //Uploader will find apk file with name contains tag field.
        tag = 'pgyer'
        forTest = false
        //Your pgyer account's uKey value.
        uKey = "xxxx"
        //Your pgyer account's _api_key value.
        _api_key = "xxx"
        installType = '1'
        updateDescription = "Upload."
    }
}
```

Define your upload task in module project build.gradle file.

```groovy

import com.catpaw.plugins.tasks.PgyerUploaderTask

task uploadPgyerArchivesHeavy(type: PgyerUploaderTask) {
    group 'uploader'
    dependsOn 'apkRelease'
    doLast {
        println 'done.'
    }
}

task uploadPgyerArchivesLight(type: PgyerUploaderTask) {
    group 'uploader'
    doLast {
        println 'done.'
    }
}
```








