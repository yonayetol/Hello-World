class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)
        
        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            
            for file_info in parts[1:]:
                file_name, content = file_info.split('(')
                content = content[:-1]
                full_path = f"{directory}/{file_name}"
                content_map[content].append(full_path)

        return [paths for paths in content_map.values() if len(paths) > 1]
