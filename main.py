import rumps
import subprocess

# global variables
selected_folder_path = ""

def select_folder():
    global selected_folder_path
    try:
        applescript = '''
        tell application "Finder"
            set folderSelection to choose folder with prompt "Please select your git folder"
            return POSIX path of folderSelection
        end tell
        '''
        selected_folder_path = subprocess.check_output(["osascript", "-e", applescript]).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        return False
    return True

def verify_git_repo():
    global selected_folder_path
    if not selected_folder_path:
        return "Select a folder first"
    try:
        result = subprocess.run(["git", "-C", selected_folder_path, "status", "--porcelain"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        changes = result.stdout.decode().strip().split('\n') if result.stdout.decode().strip() else []
        if changes:
            return f"🟢 Sync Changes ({len(changes)})"
        else:
            return "No changes detected"
    except subprocess.CalledProcessError:
        return "🚫 Not a Git repo"

def sync_changes(commit_message):
    global selected_folder_path
    if not selected_folder_path:
        return "📁 Select a folder first"
    try:
        subprocess.check_call(["git", "-C", selected_folder_path, "fetch"], stderr=subprocess.STDOUT)
        subprocess.check_call(["git", "-C", selected_folder_path, "pull"], stderr=subprocess.STDOUT)
        subprocess.check_call(["git", "-C", selected_folder_path, "add", "."], stderr=subprocess.STDOUT)
        subprocess.check_call(["git", "-C", selected_folder_path, "commit", "-m", commit_message], stderr=subprocess.STDOUT)

        subprocess.check_call(["git", "-C", selected_folder_path, "push"], stderr=subprocess.STDOUT)
        return "✅ Sync Changes"
    except subprocess.CalledProcessError:
        return "🚫 Sync Changes"

class MenubarApp(rumps.App):
    def __init__(self):
        super(MenubarApp, self).__init__("EasyGit")
        self.menu = ["Select Folder", "Sync Changes", "Enter Commit Message..."]
        self.icon = "icon.png"
        self.folder_path = None
        self.verify_timer = rumps.Timer(self.auto_verify_repo, 5)
        self.verify_timer.start()

    @rumps.clicked("Select Folder")
    def select_folder(self, _):
        global selected_folder_path
        success = select_folder()
        if success:
            self.menu['Select Folder'].title = f"{selected_folder_path}"
            self.auto_verify_repo(None)
        else:
            self.menu['Select Folder'].title = f"Select Folder"

    @rumps.clicked("Sync Changes")
    def sync(self, _):
        # Since direct input is not supported, we initiate sync here if commit message is already set.
        commit_message = rumps.Window(title="Commit Message Required",
                                      message="Please enter the commit message via 'Enter Commit Message...' menu option first.",
                                      ok=None).run()
        # Placeholder for sync logic if commit message is already set.
        # sync_status = sync_changes(commit_message)
        # self.menu['Sync Changes'].title = sync_status

    @rumps.clicked("Enter Commit Message...")
    def enter_commit_message(self, _):
        commit_message = rumps.Window(title="Enter Commit Message",
                                      message="Enter the commit message for your changes:",
                                      default_text="").run()
        if commit_message.clicked:
            sync_status = sync_changes(commit_message.text)
            rumps.alert(title="Sync Status", message=sync_status)

    def check_status(self, _):
        status = verify_git_repo()
        self.menu['Sync Changes'].title = status

    def auto_verify_repo(self, sender):
        status = verify_git_repo()
        self.menu['Sync Changes'].title = status

if __name__ == "__main__":
    MenubarApp().run()
