import shlex

from .utils import run_command

APPTAINER_VERSION = "apptainer version 1.2.4-1.el7"


class PytainerOptions:
    def __init__(self):
        self.options = []

    def to_string(self):
        return " ".join(self.options)

    def add(self, option):
        self.options.append(option)

    def add_all(self, options):
        self.options.extend(options)

    def remove(self, option):
        self.options.remove(option)

    def shell_escape(self, string):
        return shlex.quote(string)


class PytainerOptionsExec(PytainerOptions):
    """
    Run a command within a container

    Usage:
      apptainer exec [exec options...] <container> <command>

    Description:
      apptainer exec supports the following formats:

      *.sif               Singularity Image Format (SIF). Native to Singularity
                          (3.0+) and Apptainer (v1.0.0+)

      *.sqsh              SquashFS format.  Native to Singularity 2.4+

      *.img               ext3 format. Native to Singularity versions < 2.4.

      directory/          sandbox format. Directory containing a valid root file
                          system and optionally Apptainer meta-data.

      instance://*        A local running instance of a container. (See the instance
                          command group.)

      library://*         A SIF container hosted on a Library (no default)

      docker://*          A Docker/OCI container hosted on Docker Hub or another
                          OCI registry.

      shub://*            A container hosted on Singularity Hub.

      oras://*            A SIF container hosted on an OCI registry that supports
                          the OCI Registry As Storage (ORAS) specification.

    Options:
          --add-caps string               a comma separated capability list to add
          --allow-setuid                  allow setuid binaries in container
                                          (root only)
          --app string                    set an application to run inside a
                                          container
          --apply-cgroups string          apply cgroups from file for
                                          container processes (root only)
      -B, --bind stringArray              a user-bind path specification.
                                          spec has the format
                                          src[:dest[:opts]], where src and
                                          dest are outside and inside paths.
                                          If dest is not given, it is set
                                          equal to src.  Mount options
                                          ('opts') may be specified as 'ro'
                                          (read-only) or 'rw' (read/write,
                                          which is the default). Multiple bind
                                          paths can be given by a comma
                                          separated list.
          --blkio-weight int              Block IO relative weight in range
                                          10-1000, 0 to disable
          --blkio-weight-device strings   Device specific block IO relative weight
      -e, --cleanenv                      clean environment before running
                                          container
          --compat                        apply settings for increased
                                          OCI/Docker compatibility. Infers
                                          --containall, --no-init, --no-umask,
                                          --no-eval, --writable-tmpfs.
      -c, --contain                       use minimal /dev and empty other
                                          directories (e.g. /tmp and $HOME)
                                          instead of sharing filesystems from
                                          your host
      -C, --containall                    contain not only file systems, but
                                          also PID, IPC, and environment
          --cpu-shares int                CPU shares for container (default -1)
          --cpus string                   Number of CPUs available to container
          --cpuset-cpus string            List of host CPUs available to container
          --cpuset-mems string            List of host memory nodes available
                                          to container
          --disable-cache                 do not use or create cache
          --dns string                    list of DNS server separated by
                                          commas to add in resolv.conf
          --docker-host string            specify a custom Docker daemon host
          --docker-login                  login to a Docker Repository
                                          interactively
          --drop-caps string              a comma separated capability list to drop
          --env stringToString            pass environment variable to
                                          contained process (default [])
          --env-file string               pass environment variables from file
                                          to contained process
      -f, --fakeroot                      run container with the appearance of
                                          running as root
          --fusemount strings             A FUSE filesystem mount
                                          specification of the form
                                          '<type>:<fuse command> <mountpoint>'
                                          - where <type> is 'container' or
                                          'host', specifying where the mount
                                          will be performed
                                          ('container-daemon' or 'host-daemon'
                                          will run the FUSE process detached).
                                          <fuse command> is the path to the
                                          FUSE executable, plus options for
                                          the mount. <mountpoint> is the
                                          location in the container to which
                                          the FUSE mount will be attached.
                                          E.g. 'container:sshfs 10.0.0.1:/
                                          /sshfs'. Implies --pid.
      -h, --help                          help for exec
      -H, --home string                   a home directory specification.
                                          spec can either be a src path or
                                          src:dest pair.  src is the source
                                          path of the home directory outside
                                          the container and dest overrides the
                                          home directory within the container.
                                          (default "/home/yohan")
          --hostname string               set container hostname
      -i, --ipc                           run container in a new IPC namespace
          --keep-privs                    let root user keep privileges in
                                          container (root only)
          --memory string                 Memory limit in bytes
          --memory-reservation string     Memory soft limit in bytes
          --memory-swap string            Swap limit, use -1 for unlimited swap
          --mount stringArray             a mount specification e.g.
                                          'type=bind,source=/opt,destination=/hostopt'.
      -n, --net                           run container in a new network
                                          namespace (sets up a bridge network
                                          interface by default)
          --network string                specify desired network type
                                          separated by commas, each network
                                          will bring up a dedicated interface
                                          inside container
          --network-args strings          specify network arguments to pass to
                                          CNI plugins
          --no-eval                       do not shell evaluate env vars or
                                          OCI container CMD/ENTRYPOINT/ARGS
          --no-home                       do NOT mount users home directory if
                                          /home is not the current working
                                          directory
          --no-https                      use http instead of https for
                                          docker:// oras:// and
                                          library://<hostname>/... URIs
          --no-init                       do NOT start shim process with --pid
          --no-mount strings              disable one or more 'mount xxx'
                                          options set in apptainer.conf and/or
                                          specify absolute destination path to
                                          disable a bind path entry, or
                                          'bind-paths' to disable all bind
                                          path entries.
          --no-privs                      drop all privileges from root user
                                          in container)
          --no-umask                      do not propagate umask to the
                                          container, set default 0022 umask
          --nv                            enable Nvidia support
          --nvccli                        use nvidia-container-cli for GPU
                                          setup (experimental)
          --oom-kill-disable              Disable OOM killer
      -o, --overlay strings               use an overlayFS image for
                                          persistent data storage or as
                                          read-only layer of container
          --passphrase                    prompt for an encryption passphrase
          --pem-path string               enter an path to a PEM formatted RSA
                                          key for an encrypted container
      -p, --pid                           run container in a new PID namespace
          --pids-limit int                Limit number of container PIDs, use
                                          -1 for unlimited
          --pwd string                    initial working directory for
                                          payload process inside the container
          --rocm                          enable experimental Rocm support
      -S, --scratch strings               include a scratch directory within
                                          the container that is linked to a
                                          temporary dir (use -W to force location)
          --security strings              enable security features (SELinux,
                                          Apparmor, Seccomp)
          --underlay                      use underlay
          --unsquash                      Convert SIF file to temporary
                                          sandbox before running
      -u, --userns                        run container in a new user namespace
          --uts                           run container in a new UTS namespace
          --vm                            enable VM support
          --vm-cpu string                 number of CPU cores to allocate to
                                          Virtual Machine (implies --vm)
                                          (default "1")
          --vm-err                        enable attaching stderr from VM
          --vm-ip string                  IP Address to assign for container
                                          usage. Defaults to DHCP within
                                          bridge network. (default "dhcp")
          --vm-ram string                 amount of RAM in MiB to allocate to
                                          Virtual Machine (implies --vm)
                                          (default "1024")
      -W, --workdir string                working directory to be used for
                                          /tmp, /var/tmp and $HOME (if
                                          -c/--contain was also used)
      -w, --writable                      by default all Apptainer containers
                                          are available as read only. This
                                          option makes the file system
                                          accessible as read/write.
          --writable-tmpfs                makes the file system accessible as
                                          read-write with non persistent data
                                          (with overlay support only)
    """

    def __init__(self):
        super().__init__()

    def add_caps(self, caps):
        self.add(f"--add-caps {caps}")

    def allow_setuid(self):
        self.add("--allow-setuid")

    def app(self, app):
        self.add(f"--app {app}")

    def apply_cgroups(self, cgroups):
        self.add(f"--apply-cgroups {cgroups}")

    def bind(self, src, dest=None, opts=None):
        dest = dest or src
        opts = opts or "rw"
        self.add(f"-B {src}:{dest}:{opts}")

    def blkio_weight(self, weight):
        assert isinstance(weight, int) and 10 <= weight <= 1000
        self.add(f"--blkio-weight {weight}")

    def blkio_weight_device(self, devices):
        self.add(f"--blkio-weight-device {devices}")

    def cleanenv(self):
        self.add("--cleanenv")

    def compat(self):
        self.add("--compat")

    def contain(self):
        self.add("--contain")

    def containall(self):
        self.add("--containall")

    def cpu_shares(self, shares):
        shares = shares or -1
        self.add(f"--cpu-shares {shares}")

    def cpus(self, cpus):
        self.add(f"--cpus {cpus}")

    def cpuset_cpus(self, cpus):
        self.add(f"--cpuset-cpus {cpus}")

    def cpuset_mems(self, mems):
        self.add(f"--cpuset-mems {mems}")

    def disable_cache(self):
        self.add("--disable-cache")

    def dns(self, dns):
        self.add(f"--dns {dns}")

    def docker_host(self, docker_host):
        self.add(f"--docker-host {docker_host}")

    def docker_login(self):
        self.add("--docker-login")

    def drop_caps(self, caps):
        self.add(f"--drop-caps {caps}")

    def env(self, name, value, escape=True):
        value = self.shell_escape(value) if escape else value
        self.add(f"-e {name}={value}")

    def env_file(self, env_file):
        self.add(f"--env-file {env_file}")

    def fakeroot(self):
        self.add("--fakeroot")

    def fusemount(self, fusemount):
        self.add(f"--fusemount {fusemount}")

    def help(self):
        self.add("--help")

    def home(self, home):
        self.add(f"--home {home}")

    def hostname(self, hostname):
        self.add(f"--hostname {hostname}")

    def ipc(self):
        self.add("--ipc")

    def keep_privs(self):
        self.add("--keep-privs")

    def memory(self, memory):
        self.add(f"--memory {memory}")

    def memory_reservation(self, memory_reservation):
        self.add(f"--memory-reservation {memory_reservation}")

    def memory_swap(self, memory_swap):
        self.add(f"--memory-swap {memory_swap}")

    def mount(self, mount):
        self.add(f"--mount {mount}")

    def net(self):
        self.add("--net")

    def network(self, network):
        self.add(f"--network {network}")

    def network_args(self, network_args):
        self.add(f"--network-args {network_args}")

    def no_eval(self):
        self.add("--no-eval")

    def no_home(self):
        self.add("--no-home")

    def no_https(self):
        self.add("--no-https")

    def no_init(self):
        self.add("--no-init")

    def no_mount(self, mount):
        self.add(f"--no-mount {mount}")

    def no_privs(self):
        self.add("--no-privs")

    def no_umask(self):
        self.add("--no-umask")

    def nv(self):
        self.add("--nv")

    def nvccli(self):
        self.add("--nvccli")

    def oom_kill_disable(self):
        self.add("--oom-kill-disable")

    def overlay(self, overlay):
        self.add(f"--overlay {overlay}")

    def passphrase(self):
        self.add("--passphrase")

    def pem_path(self, pem_path):
        self.add(f"--pem-path {pem_path}")

    def pid(self):
        self.add("--pid")

    def pids_limit(self, pids_limit):
        self.add(f"--pids-limit {pids_limit}")

    def pwd(self, pwd):
        self.add(f"--pwd {pwd}")

    def rocm(self):
        self.add("--rocm")

    def scratch(self, scratch):
        self.add(f"--scratch {scratch}")

    def security(self, security):
        self.add(f"--security {security}")

    def underlay(self):
        self.add("--underlay")

    def unsquash(self):
        self.add("--unsquash")

    def userns(self):
        self.add("--userns")

    def uts(self):
        self.add("--uts")

    def vm(self):
        self.add("--vm")

    def vm_cpu(self, vm_cpu):
        self.add(f"--vm-cpu {vm_cpu}")

    def vm_err(self):
        self.add("--vm-err")

    def vm_ip(self, vm_ip):
        self.add(f"--vm-ip {vm_ip}")

    def vm_ram(self, vm_ram):
        self.add(f"--vm-ram {vm_ram}")

    def workdir(self, workdir):
        self.add(f"--workdir {workdir}")

    def writable(self):
        self.add("--writable")

    def writable_tmpfs(self):
        self.add("--writable-tmpfs")


class PytainerOptionsPull(PytainerOptions):
    """
    Pull an image from a URI

    Usage:
      apptainer pull [pull options...] [output file] <URI>

    Description:
      The 'pull' command allows you to download or build a container from a given
      URI. Supported URIs include:

      library: Pull an image from the currently configured library
          library://user/collection/container[:tag]

      docker: Pull a Docker/OCI image from Docker Hub, or another OCI registry.
          docker://user/image:tag

      shub: Pull an image from Singularity Hub
          shub://user/image:tag

      oras: Pull a SIF image from an OCI registry that supports ORAS.
          oras://registry/namespace/image:tag

      http, https: Pull an image using the http(s?) protocol
          https://example.com/alpine.sif

    Options:
          --arch string           architecture to pull from library (default
                                  "amd64")
          --arch-variant string   architecture variant to pull from library
          --dir string            download images to the specific directory
          --disable-cache         do not use or create cached images/blobs
          --docker-host string    specify a custom Docker daemon host
          --docker-login          login to a Docker Repository interactively
      -F, --force                 overwrite an image file if it exists
      -h, --help                  help for pull
          --library string        download images from the provided library
          --no-cleanup            do NOT clean up bundle after failed build,
                                  can be helpful for debugging
          --no-https              use http instead of https for docker://
                                  oras:// and library://<hostname>/... URIs
    """

    def __init__(self):
        super().__init__()

    def arch(self, arch):
        self.add(f"--arch {arch}")

    def arch_variant(self, arch_variant):
        self.add(f"--arch-variant {arch_variant}")

    def dir(self, dir):
        self.add(f"--dir {dir}")

    def disable_cache(self):
        self.add("--disable-cache")

    def docker_host(self, docker_host):
        self.add(f"--docker-host {docker_host}")

    def docker_login(self):
        self.add("--docker-login")

    def force(self):
        self.add("--force")

    def library(self, library):
        self.add(f"--library {library}")

    def no_cleanup(self):
        self.add("--no-cleanup")

    def no_https(self):
        self.add("--no-https")


class PytainerOptionsBuild(PytainerOptions):
    """
    Build an Apptainer image

    Usage:
      apptainer build [local options...] <IMAGE PATH> <BUILD SPEC>

    Description:

      IMAGE PATH:

      When Apptainer builds the container, output can be one of a few formats:

          default:    The compressed Apptainer read only image format (default)
          sandbox:    This is a read-write container within a directory structure

      note: It is a common workflow to use the "sandbox" mode for development of the
      container, and then build it as a default Apptainer image for production
      use. The default format is immutable.

      BUILD SPEC:

      The build spec target is a definition (def) file, local image, or URI that can
      be used to create an Apptainer container. Several different local target
      formats exist:

          def file  : This is a recipe for building a container (examples below)
          directory:  A directory structure containing a (ch)root file system
          image:      A local image on your machine (will convert to sif if
                      it is legacy format)

      Targets can also be remote and defined by a URI of the following formats:

          library://  an image library (no default)
          docker://   a Docker/OCI registry (default Docker Hub)
          shub://     an Apptainer registry (default Singularity Hub)
          oras://     an OCI registry that holds SIF files using ORAS

      Temporary files:

      The location used for temporary directories defaults to '/tmp' but
      can be overridden by the TMPDIR environment variable, and that can be
      overridden by the APPTAINER_TMPDIR environment variable.  The
      temporary directory used during a build must be on a filesystem that
      has enough space to hold the entire container image, uncompressed,
      including any temporary files that are created and later removed
      during the build. You may need to set APPTAINER_TMPDIR or TMPDIR when
      building a large container on a system that has a small /tmp filesystem.

    Options:
      -B, --bind stringArray         a user-bind path specification. spec has
                                     the format src[:dest[:opts]],where src
                                     and dest are outside and inside paths. If
                                     dest is not given,it is set equal to src.
                                     Mount options ('opts') may be specified
                                     as 'ro'(read-only) or 'rw' (read/write,
                                     which is the default).Multiple bind paths
                                     can be given by a comma separated list.
          --build-arg strings        defines variable=value to replace {{
                                     variable }} entries in build definition file
          --build-arg-file string    specifies a file containing
                                     variable=value lines to replace '{{
                                     variable }}' with value in build
                                     definition files
          --disable-cache            do not use cache or create cache
          --docker-host string       specify a custom Docker daemon host
          --docker-login             login to a Docker Repository interactively
      -e, --encrypt                  build an image with an encrypted file system
      -f, --fakeroot                 build with the appearance of running as
                                     root (default when building from a
                                     definition file unprivileged)
          --fix-perms                ensure owner has rwX permissions on all
                                     container content for oci/docker sources
      -F, --force                    overwrite an image file if it exists
      -h, --help                     help for build
          --json                     interpret build definition as JSON
          --library string           container Library URL
          --mount stringArray        a mount specification e.g.
                                     'type=bind,source=/opt,destination=/hostopt'.
          --no-cleanup               do NOT clean up bundle after failed
                                     build, can be helpful for debugging
          --no-https                 use http instead of https for docker://
                                     oras:// and library://<hostname>/... URIs
      -T, --notest                   build without running tests in %test section
          --nv                       inject host Nvidia libraries during build
                                     for post and test sections
          --nvccli                   use nvidia-container-cli for GPU setup
                                     (experimental)
          --passphrase               prompt for an encryption passphrase
          --pem-path string          enter an path to a PEM formatted RSA key
                                     for an encrypted container
          --rocm                     inject host Rocm libraries during build
                                     for post and test sections
      -s, --sandbox                  build image as sandbox format (chroot
                                     directory structure)
          --section strings          only run specific section(s) of deffile
                                     (setup, post, files, environment, test,
                                     labels, none) (default [all])
      -u, --update                   run definition over existing container
                                     (skips header)
          --userns                   build without using setuid even if available
          --warn-unused-build-args   shows warning instead of fatal message
                                     when build args are not exact matched
          --writable-tmpfs           during the %test section, makes the file
                                     system accessible as read-write with non
                                     persistent data (with overlay support only)
    """

    def __init__(self):
        super().__init__()

    def bind(self, src, dest=None, opts=None):
        dest = dest or src
        opts = opts or "rw"
        self.add(f"-B {src}:{dest}:{opts}")

    def build_arg(self, build_arg):
        self.add(f"--build-arg {build_arg}")

    def build_arg_file(self, build_arg_file):
        self.add(f"--build-arg-file {build_arg_file}")

    def disable_cache(self):
        self.add("--disable-cache")

    def docker_host(self, docker_host):
        self.add(f"--docker-host {docker_host}")

    def docker_login(self):
        self.add("--docker-login")

    def encrypt(self):
        self.add("--encrypt")

    def fakeroot(self):
        self.add("--fakeroot")

    def fix_perms(self):
        self.add("--fix-perms")

    def force(self):
        self.add("--force")

    def json(self):
        self.add("--json")

    def library(self, library):
        self.add(f"--library {library}")

    def mount(self, mount):
        self.add(f"--mount {mount}")

    def no_cleanup(self):
        self.add("--no-cleanup")

    def no_https(self):
        self.add("--no-https")

    def notest(self):
        self.add("--notest")

    def nv(self):
        self.add("--nv")

    def nvccli(self):
        self.add("--nvccli")

    def passphrase(self):
        self.add("--passphrase")

    def pem_path(self, pem_path):
        self.add(f"--pem-path {pem_path}")

    def rocm(self):
        self.add("--rocm")

    def sandbox(self):
        self.add("--sandbox")

    def section(self, section):
        self.add(f"--section {section}")

    def update(self):
        self.add("--update")

    def userns(self):
        self.add("--userns")

    def warn_unused_build_args(self):
        self.add("--warn-unused-build-args")

    def writable_tmpfs(self):
        self.add("--writable-tmpfs")


class PytainerOptionsInspect(PytainerOptions):
    """
    Show metadata for an image

    Usage:
      apptainer inspect [inspect options...] <image path>

    Description:
      Inspect will show you labels, environment variables, apps and scripts associated
      with the image determined by the flags you pass. By default, they will be shown in
      plain text. If you would like to list them in json format, you should use the --json flag.


    Options:
          --all           show all available data (imply --json option)
          --app string    inspect a specific app
      -d, --deffile       show the Apptainer definition file that was used to
                          generate the image
      -e, --environment   show the environment settings for the image
      -h, --help          help for inspect
      -H, --helpfile      inspect the runscript helpfile, if it exists
      -j, --json          print structured json instead of sections
      -l, --labels        show the labels for the image (default)
          --list-apps     list all apps in a container
      -r, --runscript     show the runscript for the image
      -s, --startscript   show the startscript for the image
      -t, --test          show the test script for the image
    """

    def __init__(self):
        super().__init__()

    def all(self):
        self.add("--all")

    def app(self, app):
        self.add(f"--app {app}")

    def deffile(self):
        self.add("--deffile")

    def environment(self):
        self.add("--environment")

    def helpfile(self):
        self.add("--helpfile")

    def json(self):
        self.add("--json")

    def labels(self):
        self.add("--labels")

    def list_apps(self):
        self.add("--list-apps")

    def runscript(self):
        self.add("--runscript")

    def startscript(self):
        self.add("--startscript")

    def test(self):
        self.add("--test")


class PytainerOptionsRun(PytainerOptions):
    """
    Run the user-defined default command within a container

    Usage:
      apptainer run [run options...] <container> [args...]

    Description:
      This command will launch an Apptainer container and execute a runscript
      if one is defined for that container. The runscript is a metadata file within
      the container that contains shell commands. If the file is present (and
      executable) then this command will execute that file within the container
      automatically. All arguments following the container name will be passed
      directly to the runscript.

      apptainer run accepts the following container formats:

      *.sif               Singularity Image Format (SIF). Native to Singularity
                          (3.0+) and Apptainer (v1.0.0+)

      *.sqsh              SquashFS format.  Native to Singularity 2.4+

      *.img               ext3 format. Native to Singularity versions < 2.4.

      directory/          sandbox format. Directory containing a valid root file
                          system and optionally Apptainer meta-data.

      instance://*        A local running instance of a container. (See the instance
                          command group.)

      library://*         A SIF container hosted on a Library (no default)

      docker://*          A Docker/OCI container hosted on Docker Hub or another
                          OCI registry.

      shub://*            A container hosted on Singularity Hub.

      oras://*            A SIF container hosted on an OCI registry that supports
                          the OCI Registry As Storage (ORAS) specification.

    Options:
          --add-caps string               a comma separated capability list to add
          --allow-setuid                  allow setuid binaries in container
                                          (root only)
          --app string                    set an application to run inside a
                                          container
          --apply-cgroups string          apply cgroups from file for
                                          container processes (root only)
      -B, --bind stringArray              a user-bind path specification.
                                          spec has the format
                                          src[:dest[:opts]], where src and
                                          dest are outside and inside paths.
                                          If dest is not given, it is set
                                          equal to src.  Mount options
                                          ('opts') may be specified as 'ro'
                                          (read-only) or 'rw' (read/write,
                                          which is the default). Multiple bind
                                          paths can be given by a comma
                                          separated list.
          --blkio-weight int              Block IO relative weight in range
                                          10-1000, 0 to disable
          --blkio-weight-device strings   Device specific block IO relative weight
      -e, --cleanenv                      clean environment before running
                                          container
          --compat                        apply settings for increased
                                          OCI/Docker compatibility. Infers
                                          --containall, --no-init, --no-umask,
                                          --no-eval, --writable-tmpfs.
      -c, --contain                       use minimal /dev and empty other
                                          directories (e.g. /tmp and $HOME)
                                          instead of sharing filesystems from
                                          your host
      -C, --containall                    contain not only file systems, but
                                          also PID, IPC, and environment
          --cpu-shares int                CPU shares for container (default -1)
          --cpus string                   Number of CPUs available to container
          --cpuset-cpus string            List of host CPUs available to container
          --cpuset-mems string            List of host memory nodes available
                                          to container
          --disable-cache                 do not use or create cache
          --dns string                    list of DNS server separated by
                                          commas to add in resolv.conf
          --docker-host string            specify a custom Docker daemon host
          --docker-login                  login to a Docker Repository
                                          interactively
          --drop-caps string              a comma separated capability list to drop
          --env stringToString            pass environment variable to
                                          contained process (default [])
          --env-file string               pass environment variables from file
                                          to contained process
      -f, --fakeroot                      run container with the appearance of
                                          running as root
          --fusemount strings             A FUSE filesystem mount
                                          specification of the form
                                          '<type>:<fuse command> <mountpoint>'
                                          - where <type> is 'container' or
                                          'host', specifying where the mount
                                          will be performed
                                          ('container-daemon' or 'host-daemon'
                                          will run the FUSE process detached).
                                          <fuse command> is the path to the
                                          FUSE executable, plus options for
                                          the mount. <mountpoint> is the
                                          location in the container to which
                                          the FUSE mount will be attached.
                                          E.g. 'container:sshfs 10.0.0.1:/
                                          /sshfs'. Implies --pid.
      -h, --help                          help for run
      -H, --home string                   a home directory specification.
                                          spec can either be a src path or
                                          src:dest pair.  src is the source
                                          path of the home directory outside
                                          the container and dest overrides the
                                          home directory within the container.
                                          (default "/home/yohan")
          --hostname string               set container hostname
      -i, --ipc                           run container in a new IPC namespace
          --keep-privs                    let root user keep privileges in
                                          container (root only)
          --memory string                 Memory limit in bytes
          --memory-reservation string     Memory soft limit in bytes
          --memory-swap string            Swap limit, use -1 for unlimited swap
          --mount stringArray             a mount specification e.g.
                                          'type=bind,source=/opt,destination=/hostopt'.
      -n, --net                           run container in a new network
                                          namespace (sets up a bridge network
                                          interface by default)
          --network string                specify desired network type
                                          separated by commas, each network
                                          will bring up a dedicated interface
                                          inside container
          --network-args strings          specify network arguments to pass to
                                          CNI plugins
          --no-eval                       do not shell evaluate env vars or
                                          OCI container CMD/ENTRYPOINT/ARGS
          --no-home                       do NOT mount users home directory if
                                          /home is not the current working
                                          directory
          --no-https                      use http instead of https for
                                          docker:// oras:// and
                                          library://<hostname>/... URIs
          --no-init                       do NOT start shim process with --pid
          --no-mount strings              disable one or more 'mount xxx'
                                          options set in apptainer.conf and/or
                                          specify absolute destination path to
                                          disable a bind path entry, or
                                          'bind-paths' to disable all bind
                                          path entries.
          --no-privs                      drop all privileges from root user
                                          in container)
          --no-umask                      do not propagate umask to the
                                          container, set default 0022 umask
          --nv                            enable Nvidia support
          --nvccli                        use nvidia-container-cli for GPU
                                          setup (experimental)
          --oom-kill-disable              Disable OOM killer
      -o, --overlay strings               use an overlayFS image for
                                          persistent data storage or as
                                          read-only layer of container
          --passphrase                    prompt for an encryption passphrase
          --pem-path string               enter an path to a PEM formatted RSA
                                          key for an encrypted container
      -p, --pid                           run container in a new PID namespace
          --pids-limit int                Limit number of container PIDs, use
                                          -1 for unlimited
          --pwd string                    initial working directory for
                                          payload process inside the container
          --rocm                          enable experimental Rocm support
      -S, --scratch strings               include a scratch directory within
                                          the container that is linked to a
                                          temporary dir (use -W to force location)
          --security strings              enable security features (SELinux,
                                          Apparmor, Seccomp)
          --underlay                      use underlay
          --unsquash                      Convert SIF file to temporary
                                          sandbox before running
      -u, --userns                        run container in a new user namespace
          --uts                           run container in a new UTS namespace
          --vm                            enable VM support
          --vm-cpu string                 number of CPU cores to allocate to
                                          Virtual Machine (implies --vm)
                                          (default "1")
          --vm-err                        enable attaching stderr from VM
          --vm-ip string                  IP Address to assign for container
                                          usage. Defaults to DHCP within
                                          bridge network. (default "dhcp")
          --vm-ram string                 amount of RAM in MiB to allocate to
                                          Virtual Machine (implies --vm)
                                          (default "1024")
      -W, --workdir string                working directory to be used for
                                          /tmp, /var/tmp and $HOME (if
                                          -c/--contain was also used)
      -w, --writable                      by default all Apptainer containers
                                          are available as read only. This
                                          option makes the file system
                                          accessible as read/write.
          --writable-tmpfs                makes the file system accessible as
                                          read-write with non persistent data
                                          (with overlay support only)

    """

    def __init__(self):
        super().__init__()

    def add_caps(self, caps):
        self.add(f"--add-caps {caps}")

    def allow_setuid(self):
        self.add("--allow-setuid")

    def app(self, app):
        self.add(f"--app {app}")

    def apply_cgroups(self, cgroups):
        self.add(f"--apply-cgroups {cgroups}")

    def bind(self, src, dest=None, opts=None):
        dest = dest or src
        opts = opts or "rw"
        self.add(f"-B {src}:{dest}:{opts}")

    def blkio_weight(self, weight):
        assert isinstance(weight, int) and 10 <= weight <= 1000
        self.add(f"--blkio-weight {weight}")

    def blkio_weight_device(self, devices):
        self.add(f"--blkio-weight-device {devices}")

    def cleanenv(self):
        self.add("--cleanenv")

    def compat(self):
        self.add("--compat")

    def contain(self):
        self.add("--contain")

    def containall(self):
        self.add("--containall")

    def cpu_shares(self, shares):
        shares = shares or -1
        self.add(f"--cpu-shares {shares}")

    def cpus(self, cpus):
        self.add(f"--cpus {cpus}")

    def cpuset_cpus(self, cpus):
        self.add(f"--cpuset-cpus {cpus}")

    def cpuset_mems(self, mems):
        self.add(f"--cpuset-mems {mems}")

    def disable_cache(self):
        self.add("--disable-cache")

    def dns(self, dns):
        self.add(f"--dns {dns}")

    def docker_host(self, docker_host):
        self.add(f"--docker-host {docker_host}")

    def docker_login(self):
        self.add("--docker-login")

    def drop_caps(self, caps):
        self.add(f"--drop-caps {caps}")

    def env(self, name, value, escape=True):
        value = self.shell_escape(value) if escape else value
        self.add(f"-e {name}={value}")

    def env_file(self, env_file):
        self.add(f"--env-file {env_file}")

    def fakeroot(self):
        self.add("--fakeroot")

    def fusemount(self, fusemount):
        self.add(f"--fusemount {fusemount}")

    def help(self):
        self.add("--help")

    def home(self, home):
        self.add(f"--home {home}")

    def hostname(self, hostname):
        self.add(f"--hostname {hostname}")

    def ipc(self):
        self.add("--ipc")

    def keep_privs(self):
        self.add("--keep-privs")

    def memory(self, memory):
        self.add(f"--memory {memory}")

    def memory_reservation(self, memory_reservation):
        self.add(f"--memory-reservation {memory_reservation}")

    def memory_swap(self, memory_swap):
        self.add(f"--memory-swap {memory_swap}")

    def mount(self, mount):
        self.add(f"--mount {mount}")

    def net(self):
        self.add("--net")

    def network(self, network):
        self.add(f"--network {network}")

    def network_args(self, network_args):
        self.add(f"--network-args {network_args}")

    def no_eval(self):
        self.add("--no-eval")

    def no_home(self):
        self.add("--no-home")

    def no_https(self):
        self.add("--no-https")

    def no_init(self):
        self.add("--no-init")

    def no_mount(self, mount):
        self.add(f"--no-mount {mount}")

    def no_privs(self):
        self.add("--no-privs")

    def no_umask(self):
        self.add("--no-umask")

    def nv(self):
        self.add("--nv")

    def nvccli(self):
        self.add("--nvccli")

    def oom_kill_disable(self):
        self.add("--oom-kill-disable")

    def overlay(self, overlay):
        self.add(f"--overlay {overlay}")

    def passphrase(self):
        self.add("--passphrase")

    def pem_path(self, pem_path):
        self.add(f"--pem-path {pem_path}")

    def pid(self):
        self.add("--pid")

    def pids_limit(self, pids_limit):
        self.add(f"--pids-limit {pids_limit}")

    def pwd(self, pwd):
        self.add(f"--pwd {pwd}")

    def rocm(self):
        self.add("--rocm")

    def scratch(self, scratch):
        self.add(f"--scratch {scratch}")

    def security(self, security):
        self.add(f"--security {security}")

    def underlay(self):
        self.add("--underlay")

    def unsquash(self):
        self.add("--unsquash")

    def userns(self):
        self.add("--userns")

    def uts(self):
        self.add("--uts")

    def vm(self):
        self.add("--vm")

    def vm_cpu(self, vm_cpu):
        self.add(f"--vm-cpu {vm_cpu}")

    def vm_err(self):
        self.add("--vm-err")

    def vm_ip(self, vm_ip):
        self.add(f"--vm-ip {vm_ip}")

    def vm_ram(self, vm_ram):
        self.add(f"--vm-ram {vm_ram}")

    def workdir(self, workdir):
        self.add(f"--workdir {workdir}")

    def writable(self):
        self.add("--writable")

    def writable_tmpfs(self):
        self.add("--writable-tmpfs")


class Pytainer:
    def __init__(self, image_path=None):
        self.image_path = image_path

    def exec(self, command, options: PytainerOptionsExec = PytainerOptionsExec()):
        cmd = ["apptainer", "exec", options.to_string(), self.image_path, command]
        return run_command(cmd)

    def pull(
        self,
        image_uri,
        save_path=None,
        options: PytainerOptionsPull = PytainerOptionsPull(),
    ):
        save_path = save_path or self.image_path
        cmd = ["apptainer", "pull", options.to_string(), save_path, image_uri]
        return run_command(cmd)

    def build(
        self,
        definition_file,
        image_path,
        options: PytainerOptionsBuild = PytainerOptionsBuild(),
    ):
        cmd = ["apptainer", "build", options.to_string(), image_path, definition_file]
        return run_command(cmd)

    def inspect(self, options: PytainerOptionsInspect = PytainerOptionsInspect()):
        cmd = ["apptainer", "inspect", options.to_string(), self.image_path]
        return run_command(cmd)

    def run(self, command, options: PytainerOptionsRun = PytainerOptionsRun()):
        cmd = ["apptainer", "run", options.to_string(), self.image_path, command]
        return run_command(cmd)

    # Additional methods can be added here for other Apptainer functionalities
