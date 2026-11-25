---
title: Safe install rules for Hermes
date: 2026-11-25
tags:
  - course
  - howto
  - hermes
  - security
  - install
status: current
canonical: true
---

# Safe install rules for Hermes

*reference implementation. Optional extension. Not required for assessment.* This is the one page for the safety rules that all install guides share. The OS guides link here and keep only what is specific to their system. See the [minimum path](../../PROJECT-WORK/01_minimum-path.md).

Facts were checked on 25 Nov 2026. A line marked *not verified* was not tested on a real machine. Read the source again before you rely on it.

Provider and key table: in section 3 of each OS guide. OS guides: [Windows](../01-harness-and-agents/install-windows.md) · [macOS](../01-harness-and-agents/install-mac.md) · [Linux](../01-harness-and-agents/install-linux.md). Advanced: [Docker sandbox](howto-hermes-docker-sandbox.md).

## 1. What protects you, and what does not

Hermes runs as your own OS user. Its terminal tool runs as the same user. Approvals and file guards are a guardrail against an honest mistake. They are not a sandbox against a hostile program. For containment, use an isolated backend such as Docker. Source: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine

On by default, from the same page:

- Dangerous shell commands need approval. The default mode is `smart`. Unanswered prompts are denied after 300 seconds.
- A hardline blocklist refuses commands such as `rm -rf /`, in every mode.
- The file tools cannot write to credential stores (`~/.ssh`, `~/.aws`, `.env` files, Hermes `auth.json`).
- Secrets that look like keys are redacted from tool output.
- Hermes sends no telemetry. Calls go only to the provider you choose.
- The messaging gateway denies every user who is not on an allowlist or paired.

Not covered:

- A file write inside your folders gets no prompt.
- Hermes can read every file that your user can read.
- The guards do not limit the terminal tool.

## 2. Privileges, by operating system

Keep these facts apart. A rule for one system is not a rule for another.

| | Account | Terminal | Elevation, only for a named step | Never |
|---|---|---|---|---|
| Windows | An account in the Administrators group is fine. A separate standard account is not required. | A normal, non-elevated terminal. UAC stays on. | The .NET SDK and Git for Windows installers in the vvvv example | "Run as administrator" for Hermes or the terminal. UAC set to "Never notify" |
| macOS | Your normal login account | Terminal as your user | A password prompt for a system step that you can name (see below) | `sudo` or root for Hermes or its installer |
| Linux | Your normal user | A terminal as your user | One `sudo` for a named system package step (see below) | `curl ... \| sudo bash`, `sudo hermes`, root |

Windows: Hermes needs no elevation. The details and the checks are in "Windows details" below. UAC is Windows only. Do not copy that language to macOS or Linux.

macOS: Hermes needs no root. Two steps can ask for a password:

- Copying `Hermes.app` to Applications, if your account is not an administrator. You can use `~/Applications` instead. The Hermes updater looks in both places (Hermes updating page). Updates from `~/Applications`: not verified.
- The command-line installer, when Git is missing. `install.sh` runs `brew install git` or `xcode-select --install` (script text, read 25 Nov 2026). Whether Apple's installer asks for a password: not verified.

Linux: the command-line installer can run `sudo -v` once, only when Node.js needs the `libatomic` package and your terminal can answer a prompt (script text and Hermes install page). Read the prompt. Enter your password for that one step. Do not put `sudo` in front of the installer.

### Windows details

An account in the Administrators group has two tokens when User Account Control (UAC) is on. A token is the list of rights that a program gets. Windows starts Explorer and your normal terminal with the filtered token. That token works like a standard user. Windows uses the full token only when you approve a UAC prompt. Source: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works (checked 25 Nov 2026).

Know these limits:

- Microsoft calls a standard account the more secure way to run Windows. An administrator account in Admin Approval Mode is a supported second choice. For work with real data, a standard daily account is the better habit.
- UAC is not a security boundary. Microsoft says so: https://learn.microsoft.com/en-us/archive/blogs/e7/update-on-uac
- Hermes runs as your Windows user, with or without a UAC prompt. A normal terminal can still read and change your own files. Hermes approvals are a guardrail for honest mistakes. They are not a sandbox.
- Some Windows 11 computers use "Administrator protection". It is off by default. Microsoft says that a security baseline can turn it on. With it, an elevated program runs as a hidden second account with its own profile. Anything you install in an elevated window may land in that other profile. This is one more reason to install without elevation. Source: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/administrator-protection/ (whether it is on for the test computer: not verified).

What each install method does, checked 25 Nov 2026:

| | Hermes Desktop (MSIX, `.appinstaller`) | Hermes Desktop (Microsoft Store) | Command-line script `install.ps1` |
|---|---|---|---|
| Scope | Per user (Microsoft: MSIX installs per user) | Per user, Store-owned | Per user |
| Needs elevation | No (not verified on a real machine) | No (not verified on a real machine) | No. Hermes docs say "No admin rights required". The script has no administrator check or UAC call |
| Program files | Inside the package. Windows keeps package files under `C:\Program Files\WindowsApps` and locks them | The same | `%LOCALAPPDATA%\hermes\hermes-agent\` |
| Your data | `%LOCALAPPDATA%\hermes\` (Hermes docs; not verified for the Store package) | The same | `%LOCALAPPDATA%\hermes\` |
| Signature | Signed bundle. Publisher in the build files: `CN=Nous Research Inc.` | Store signs it. Publisher name: not verified | None on the script. It checks the SHA-256 hash of the uv and Git files that it downloads. Hermes publishes no checksum for `install.ps1` (not found) |
| Hosts | Hermes download page | Microsoft Store | `github.com`, `api.github.com`, `hermes-assets.nousresearch.com` (script text). Later steps may use more hosts (not verified) |
| Update | The Update control in Hermes, through Windows App Installer | Microsoft Store | `hermes update` |
| Remove | Windows Settings, Apps, Installed apps | The same | `hermes uninstall` |
| Changes to PATH | Execution aliases (`hermes`, `hermes-agent`, `hermes-acp`) | The same | Your user `Path` only |

Sources: https://hermes-agent.nousresearch.com/docs/getting-started/installation, https://hermes-agent.nousresearch.com/docs/user-guide/windows-native, https://hermes-agent.nousresearch.com/docs/getting-started/updating, the Hermes desktop build notes (`apps/desktop/BUILDING.md` in the Hermes repository), and Microsoft: https://learn.microsoft.com/en-us/windows/msix/desktop/desktop-to-uwp-behind-the-scenes

Checks on Windows. A line that starts with STOP means: stop, do not continue, and tell the teacher.

1. Keep UAC on. Search the Start menu for "Change User Account Control settings". Leave the slider at its default. Do not choose "Never notify". With that setting Windows still gives you a split token but approves every elevation for you (Microsoft Win32 UAC page).
2. Open a normal Windows Terminal. Type `whoami /groups | Select-String "Mandatory Label"` and press Enter. The line must say `Medium Mandatory Level`. STOP if it says `High Mandatory Level`. Close the window and open a normal one.
3. Check the host name in the address bar of the download page: `hermes-agent.nousresearch.com`. STOP if it is another host.
4. Read the Windows App Installer window before you click Install. The publisher must be Nous Research. How the window shows the publisher: not verified. STOP if the publisher is another name, or if the file is not signed.
5. After the install, type `Get-AppxPackage *hermes* | Format-List Name, Publisher, SignatureKind, InstallLocation` in the normal terminal. For the `.appinstaller` package, expect a Publisher that contains `CN=Nous Research Inc.`. The value of `SignatureKind` is not verified. Write down what you see.
6. STOP if any UAC prompt appears while you install or start Hermes Desktop. No official page says Hermes Desktop needs one. Click No.
7. Elevate only for a named step. In the install guide, only the vvvv example may ask for UAC:
   - The .NET SDK installer. Microsoft says the native installer installs system-wide and needs administrator rights.
   - The Git for Windows installer. For an administrator account it asks for UAC and installs to `C:\Program Files\Git` (Git for Windows installer script). Hermes does not need it. You need it only for the `git clone` step in the example.
   - Node.js: not verified.

   Read the UAC window. It must show a verified publisher. Click Yes for that one installer. Then close the installer and go back to your normal terminal. Do not keep an elevated window open.

Not verified, on a real Windows 11 Enterprise 25H2 machine: the items marked above, the label of every window, and whether company policy blocks sideloaded packages. Windows 11 has sideloading on by default (Microsoft Learn). If App Installer says it is blocked, STOP and use the Microsoft Store button. Do not change a policy to make it work.

## 3. Check the download

1. Use only the official host: `hermes-agent.nousresearch.com`. Hermes lists its official domains: https://hermes-agent.nousresearch.com/docs/getting-started/official-domains
2. Prefer a Desktop package over a script. A package is a file you open. A script piped into a shell runs before you can read it.
3. For a script, use path B in the OS guide: save it, read it, then run it. Hermes publishes no checksum for `install.sh` or `install.ps1` (not found). The scripts check the SHA-256 hash of the uv and Git files that they download. That does not prove that the script is the official file.
4. Class check, not an official hash: the teacher computes a hash of the saved script on the same day (`Get-FileHash` on Windows, `shasum -a 256` on macOS, `sha256sum` on Linux). Students compare it.
5. Desktop signature checks are in the OS guides: Windows (`Get-AppxPackage`), macOS (`codesign` and `spctl`). Linux has no Desktop package in a release (Hermes platform page).
6. If the OS blocks the file, or the publisher is wrong, stop. Do not turn off SmartScreen, Gatekeeper or a company policy to make it work.

## 4. The test folder

- Use the folder `hermes-smoke-test` in your home folder. Its file is public text.
- Ask Hermes to read first. Edit later.
- Do not use Documents, Desktop, Downloads, a cloud-sync folder, your vault, or a project with secrets.
- If Hermes names another folder, stop.
- Before a write task, make a Git commit or copy the folder. After the task, read the diff.
- Later, you can limit file-tool writes with `HERMES_WRITE_SAFE_ROOT`. List your Hermes home as a second root, or Hermes cannot write its own state. This does not limit the terminal tool or reads. The list separator on Windows: not verified. Source: the work-machine page above.

## 5. Secrets

- Never type or paste a key into a shell command. The shell saves it. Avoid `hermes config set OPENROUTER_API_KEY ...`, `export KEY=...` and `$env:KEY = ...`.
- Enter a key in the Hermes Settings window, at the prompt of `hermes model`, or in the `.env` file with a text editor.
- Key files: `%LOCALAPPDATA%\hermes\.env` on Windows, `~/.hermes/.env` on macOS and Linux. On macOS and Linux, `install.sh` sets that file to owner-only access (mode 600, script text). The Windows file permissions: not verified.
- PowerShell saves typed commands in `%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`. It skips lines with `password`, `token`, `apikey` and `secret`. It can still save a key. Turn saving off for one window: `Set-PSReadLineOption -HistorySaveStyle SaveNothing`. Source: https://learn.microsoft.com/en-us/powershell/module/psreadline/set-psreadlineoption
- bash and zsh skip a line that starts with a space only if you turned that on (`HISTCONTROL=ignorespace` in bash, `setopt HIST_IGNORE_SPACE` in zsh). This is a habit, not a control. Sources: the GNU Bash manual and https://zsh.sourceforge.io/Doc/Release/Options.html
- If a key reached a history file, a chat, a screenshot or Git: delete the history file and create a new key at the provider. Revoke the old key.
- Keys stay out of the vault, out of chat and out of Git.
- A free cloud model can log your prompts. Send it public text only.

## 6. Approvals

1. Type `hermes config set approvals.mode manual`.
2. Type `hermes config get approvals.mode`. The answer must be `manual`.
3. The default is `smart`. In `smart`, a helper model approves low-risk commands for you. Never set `off`.
4. Hermes does not ask before it writes a file. Use section 4.
5. Optional undo: checkpoints. Type `hermes chat --checkpoints`, or set `checkpoints.enabled: true`. In a session, `/rollback` lists them. Checkpoints are opt-in. Whether Hermes Desktop shows them: not verified.
6. Optional: your own deny rules in `approvals.deny`. They block matching commands in every mode.

Docker is advanced. It limits what a container can see. It does not add a prompt for file writes. It adds filesystem sharing, path translation, ownership, network, performance, GPU access, images, and virtualisation on Windows and macOS. It is not the two-hour baseline. See [Docker sandbox](howto-hermes-docker-sandbox.md).

## 7. The messaging gateway

Do not set up a gateway in class. It runs for a long time, as your user, and it takes messages from outside.

| System | What `hermes gateway install` does | Named admin step |
|---|---|---|
| Windows | Registers a Scheduled Task. Windows asks for UAC once. The task runs non-elevated. | None |
| Linux | Installs a systemd user service | `sudo loginctl enable-linger $USER`, or `sudo hermes gateway install --system`. Only for a host that must start at boot |
| macOS | Installs a launchd service. Whether it is a user or a system service: not verified | Not verified |

- Set an allowlist or DM pairing. The default denies all users. Never set `GATEWAY_ALLOW_ALL_USERS=true`.
- Do not expose the gateway or the Webapp to the internet. A signed-in Webapp user can run commands as your OS account.
- To stop it: `hermes gateway stop`. To remove the service on Windows: `hermes gateway uninstall`. On macOS and Linux: not verified.

Sources: https://hermes-agent.nousresearch.com/docs/user-guide/messaging, https://hermes-agent.nousresearch.com/docs/user-guide/windows-native, https://hermes-agent.nousresearch.com/docs/user-guide/desktop

## 8. Updates

Do not update during class. Each install method has one owner of its updates. Do not run Git or pip inside a signed app.

| Method | Update by |
|---|---|
| Windows Desktop, `.appinstaller` | The Update control in Hermes, through Windows App Installer |
| Windows Desktop, Store | Microsoft Store |
| macOS Desktop | The Update control in Hermes (signed ZIP) |
| Script (all systems) | `hermes update` |
| Docker | A new image (no `hermes update`) |

Whether an update needs elevation: not verified. Source: https://hermes-agent.nousresearch.com/docs/getting-started/updating

## 9. Rollback and uninstall

1. Quit Hermes. Stop a gateway first (section 7).
2. Remove the program with the method that installed it:

| Method | Remove the program | Your data stays in |
|---|---|---|
| Windows Desktop (MSIX or Store) | Windows Settings, Apps, Installed apps | `%LOCALAPPDATA%\hermes\` |
| macOS Desktop | Quit Hermes. Move `Hermes.app` to the Trash | `~/.hermes/` |
| Script, any system | `hermes uninstall --dry-run`, read the list, then `hermes uninstall` | `%LOCALAPPDATA%\hermes\` or `~/.hermes/` |

3. The command `hermes uninstall` keeps your config and data. It refuses to delete package-owned files.
4. `--full` also deletes your config, keys, chats and skills. `--data` deletes data and keeps the program. Use them only on purpose. Make a backup first: `hermes backup`. Do not delete the data folder by hand. A custom `HERMES_HOME` can sit elsewhere, and package removal does not touch it. Hermes: "Data deletion is separate from package removal."
5. Delete the `hermes-smoke-test` folder yourself.
6. Revoke the API key at the provider. Remove the key lines from the `.env` file if you keep Hermes.
7. Remove what you added in the example sections. For the vvvv example: type `dotnet tool uninstall -g vvvv-mcp` (not verified) and delete the vvvv block in `config.yaml`. Remove .NET or Git in Windows Settings, Apps, Installed apps. A UAC prompt can appear again.

Sources: https://hermes-agent.nousresearch.com/docs/getting-started/updating, https://hermes-agent.nousresearch.com/docs/user-guide/windows-native

## 10. Stop points

Stop, do not continue, and tell the teacher, if:

- The download host is not `hermes-agent.nousresearch.com`, or a script names another host.
- The OS blocks the file, or the publisher or signature is wrong.
- A password or UAC prompt appears where this page names none.
- A terminal runs elevated on Windows, or you are root on macOS or Linux.
- Hermes names your vault or another folder in the smoke test.
- A key appears in a terminal, a chat, a note or Git.

## 11. Not verified

- A real install on Windows 11 Enterprise 25H2, macOS and Linux with these rules.
- Whether a Desktop install or update asks for elevation on any system.
- The window labels of Windows App Installer and the macOS prompts.
- The Windows `.env` permissions, and the Windows list separator for `HERMES_WRITE_SAFE_ROOT`.
- The macOS gateway scope, and gateway removal on macOS and Linux.
- Whether company policy blocks sideloaded packages on a given machine.

## Sources

- https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine
- https://hermes-agent.nousresearch.com/docs/getting-started/installation
- https://hermes-agent.nousresearch.com/docs/getting-started/updating
- https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
- https://hermes-agent.nousresearch.com/docs/user-guide/messaging
- https://hermes-agent.nousresearch.com/docs/getting-started/platform-support
- Windows account facts: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works
- Course rules: [AGENTS.md](../../../AGENTS.md) · [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md)
