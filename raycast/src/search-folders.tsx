import { Action, ActionPanel, Icon, List } from "@raycast/api";
import { useState } from "react";
import { CATEGORIES, Folder, inside, lookup, tilde } from "./atlas";
import { FolderItem, missingIssueUrl, useAtlas } from "./folder-view";

export default function Command() {
  const atlas = useAtlas();
  const [text, setText] = useState("");
  const query = text.trim();
  const isPath = /^[~/]/.test(query);

  if (isPath) {
    const match = lookup(atlas, query);
    const known = match ? [] : inside(atlas, query);
    return (
      <List
        isShowingDetail={Boolean(match)}
        filtering={false}
        onSearchTextChange={setText}
        searchBarPlaceholder="Search by name, or type a path like ~/Library/Caches"
      >
        {match ? (
          <List.Section title="Match">
            <FolderItem folder={match.folder} match={match} title={tilde(match.path)} />
          </List.Section>
        ) : known.length > 0 ? (
          <List.Section title={`Not in the Atlas itself. Known folders inside ${query}`}>
            {known.map(({ folder, path }) => (
              <FolderItem key={folder.id} folder={folder} title={path} />
            ))}
          </List.Section>
        ) : (
          <List.EmptyView
            icon={Icon.QuestionMark}
            title="Not in the Atlas"
            description="Search by name instead, or ask for this folder to be added."
            actions={
              <ActionPanel>
                <Action.OpenInBrowser title="Ask for This Folder" url={missingIssueUrl(query)} />
              </ActionPanel>
            }
          />
        )}
      </List>
    );
  }

  const groups = new Map<string, Folder[]>();
  for (const f of atlas.folders) groups.set(f.category, [...(groups.get(f.category) ?? []), f]);
  const order = [...groups.keys()].sort(
    (a, b) => (CATEGORIES.indexOf(a) + 1 || 99) - (CATEGORIES.indexOf(b) + 1 || 99) || a.localeCompare(b),
  );

  return (
    <List
      isShowingDetail
      filtering
      onSearchTextChange={setText}
      searchBarPlaceholder="Search by name, or type a path like ~/Library/Caches"
    >
      {order.map((category) => (
        <List.Section key={category} title={category}>
          {(groups.get(category) ?? [])
            .sort((a, b) => a.name.localeCompare(b.name))
            .map((folder) => (
              <FolderItem key={folder.id} folder={folder} />
            ))}
        </List.Section>
      ))}
    </List>
  );
}
