System.Diagnostics.Process process = new();
System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
startInfo.FileName = "cmd.exe";
startInfo.Arguments = "/C libcamera-jpeg -o " + DateTime.Now.ToString("dd-MM-yyyyTHH-mm-ss") + ".jpg -t 0 --width 640 --height 480";
process.StartInfo = startInfo;
process.Start();

