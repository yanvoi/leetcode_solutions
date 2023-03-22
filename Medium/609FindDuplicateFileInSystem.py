class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        paths_by_content = defaultdict(list)
        for path in paths:
            directory, *files = path.split()
            for f in files:
                name, content = f.split("(")
                paths_by_content[content[:-1]].append(directory + "/" + name)

        return [diff_paths for diff_paths in paths_by_content.values() if len(diff_paths) > 1]
        
