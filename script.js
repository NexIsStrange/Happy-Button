const owner = "ctih1"; 
const repo = "Happy-Button"; 

fetch(`https://api.github.com/repos/${owner}/${repo}/releases/latest`)
  .then(response => response.json())
  .then(data => {
    const latestTag = data.tag_name;
    console.log(latestTag)
    var downloadButton = document.getElementById('download_windows');
    var downloadPortable = document.getElementById('download_windows_portable')
    window.onload = function() {
      downloadButton.setAttribute("onclick",`window.location.href="https://github.com/ctih1/Happy-Button/releases/download/${latestTag}/Happy_Button_Installer.exe"`);
      downloadPortable.setAttribute("onclick",`window.location.href="https://github.com/ctih1/Happy-Button/releases/download/${latestTag}/Windows_Portable.zip"`);
    };
      
        
    }

  )
  .catch(error => {
    console.error(`Error fetching latest release: ${error}`);
  });
  ;
