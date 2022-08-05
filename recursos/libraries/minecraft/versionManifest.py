from sys import version
import libraries.utils.request as request
import libraries.utils.system as system
import json
import logging

class versionManifest:

    def __init__(self, versions_path="versions"):
        self.versions_path = versions_path

        manifest_versions_path = "%s/%s" % (self.versions_path, "version_manifest_v2.json")

        request.download("https://launchermeta.mojang.com/mc/game/version_manifest_v2.json", manifest_versions_path, replace=True)

        json_file = open(manifest_versions_path,"r")
        self.json_loaded = json.load(json_file) 

        self.all_versions = self.json_loaded["versions"]
        self.all_versions.reverse()

    def get_lastest(self, version_type="release"):
        version = self.json_loaded["latest"][version_type]
        logging.debug("get the latest %s of Minecraft : %s" % (version_type,version))
        return version

    def get_versions(self, version_type="all"):
        # version_type : old_alpha, old_beta, snapshot, release, downloaded
        if version_type == "beta" or version_type == "b" or version_type == "old_beta":
            version_type = "old_beta"

        elif version_type == "alpha" or version_type == "a" or version_type == "old_alpha":
            version_type = "old_alpha"
        
        elif version_type == "release" or version_type == "r":
            version_type = "release"
        
        elif version_type == "downloaded" or version_type == "d":
            return self.get_downloaded_versions()

        versions = []
        for version in self.all_versions:
            if version_type != "all":
                if version_type == version["type"]:
                    versions.append(version["id"])
            else:
                versions.append(version["id"])
        
        return versions

    def exist(self, version):
        logging.debug("check if %s exist" % version)
        exist = False
        for i in self.get_downloaded_versions():
            if i == version:
                return True
        
        for i in self.get_versions():
            if i == version:
                return True
        
        if exist:
            logging.debug("%s exist" % version)
        else:
            logging.debug("%s don't exist" % version)

        return exist

    def download_versions(self, version):
        logging.debug("[version] Downloading version %s" % version)
        exist = False

        for version_ in self.all_versions:
            if version == version_["id"]:
                version_url = version_["url"]
                exist = True
                break

        if exist == False:
            return False
        version_path = "%s/%s/%s.json" % (self.versions_path, version, version)
        request.download(version_url, version_path)
        return version_path

    def get_downloaded_versions(self):
        logging.debug("check downloaded versions of Minecraft")
        folder = system.ls(self.versions_path, type="folder")
        return folder