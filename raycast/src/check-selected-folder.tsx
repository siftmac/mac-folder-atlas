import { Action, ActionPanel, Icon, List, getSelectedFinderItems } from "@raycast/api";
import { usePromise } from "@raycast/utils";
import { basename } from "path";
import { inside, lookup, tilde } from "./atlas";
import { FolderItem, missingIssueUrl, useAtlas } from "./folder-view";

export default function Command() {
  const atlas = useAtlas();
  const { data: items, isLoading, error } = usePromise(getSelectedFinderItems, [], { onError: () => undefined });

  if (error || (!isLoading && (!items || items.length === 0))) {
    return (
      <List>
        <List.EmptyView
          icon={Icon.Finder}
          title="Select a folder in Finder first"
          description="Then run this command again to see if it’s safe to delete. Or search the Atlas by name or path."
        />
      </List>
    );
  }

  return (
    <List isLoading={isLoading} isShowingDetail>
      {(items ?? []).map(({ path }) => {
        const clean = path.replace(/\/$/, "");
        const match = lookup(atlas, clean);
        if (match) return <FolderItem key={clean} folder={match.folder} match={match} title={basename(clean)} />;
        const known = inside(atlas, clean);
        const markdown =
          `# ${basename(clean)}\n\n\`${tilde(clean)}\` isn’t in the Atlas.` +
          (known.length
            ? `\n\nKnown folders inside it:\n\n${known.map((k) => `- **${k.folder.verdict_label}** \`${k.path}\`: [${k.folder.name}](${k.folder.url})`).join("\n")}`
            : "\n\nAsk for it to be added, with what you know about it.");
        return (
          <List.Item
            key={clean}
            title={basename(clean)}
            subtitle="Not in the Atlas"
            accessories={[{ tag: "?" }]}
            detail={<List.Item.Detail markdown={markdown} />}
            actions={
              <ActionPanel>
                <Action.OpenInBrowser title="Ask for This Folder" url={missingIssueUrl(clean)} />
                <Action.ShowInFinder path={clean} />
              </ActionPanel>
            }
          />
        );
      })}
    </List>
  );
}
