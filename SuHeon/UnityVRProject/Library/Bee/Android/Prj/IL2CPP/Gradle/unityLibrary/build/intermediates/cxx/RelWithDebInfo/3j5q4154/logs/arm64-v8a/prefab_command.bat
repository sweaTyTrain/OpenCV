@echo off
"C:\\Program Files\\Unity\\Hub\\Editor\\2023.2.12f1\\Editor\\Data\\PlaybackEngines\\AndroidPlayer\\OpenJDK\\bin\\java" ^
  --class-path ^
  "C:\\Users\\HoneyWater\\.gradle\\caches\\modules-2\\files-2.1\\com.google.prefab\\cli\\2.0.0\\f2702b5ca13df54e3ca92f29d6b403fb6285d8df\\cli-2.0.0-all.jar" ^
  com.google.prefab.cli.AppKt ^
  --build-system ^
  cmake ^
  --platform ^
  android ^
  --abi ^
  arm64-v8a ^
  --os-version ^
  24 ^
  --stl ^
  c++_shared ^
  --ndk-version ^
  23 ^
  --output ^
  "C:\\Users\\HoneyWater\\Desktop\\Practice\\SuHeon\\My project (1)\\.utmp\\RelWithDebInfo\\3j5q4154\\prefab\\arm64-v8a\\prefab-configure" ^
  "C:\\Users\\HoneyWater\\.gradle\\caches\\transforms-3\\6c263f9b274272e8756b525bc7d98ffe\\transformed\\jetified-games-activity-2.0.2\\prefab" ^
  "C:\\Users\\HoneyWater\\.gradle\\caches\\transforms-3\\121b6b243cedf8bef90d462440e4bf24\\transformed\\jetified-games-frame-pacing-1.10.0\\prefab"
