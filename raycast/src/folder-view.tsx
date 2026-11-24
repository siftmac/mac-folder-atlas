import { Action, ActionPanel, Color, Icon, Keyboard, List } from "@raycast/api";
import { useFetch } from "@raycast/utils";
import { ATLAS_URL, Atlas, BUNDLED, Folder, Match, REPO_URL, Verdict, exists, tilde } from "./atlas";

const COLORS: Record<Verdict, Color> = {
  rebuilds: Color.Green,
  safe: Color.Green,
  decide: Color.Yellow,
  leave: Color.Red,
};

/** The Atlas: the copy that ships with the extension at once, then the latest from GitHub when it arrives. */
export function useAtlas(): Atlas {
  const { data } = useFetch<Atlas, Atlas>(ATLAS_URL, {
    parseResponse: (response) => response.json() as Promise<Atlas>,
    initialData: BUNDLED,
    keepPreviousData: true,
    onError: () => undefined, // offline: keep the copy we have
  });
  return data && Array.isArray(data.folders) ? data : BUNDLED;
}

export function verdictTag(verdict: Verdict, label: string): List.Item.Accessory {
  return { tag: { value: label, color: COLORS[verdict] } };
}

export function folderMarkdown(folder: Folder, match?: Match): string {
  const parts = [`# ${folder.question}`];
  if (match?.note) parts.push(`> **${match.label}: \`${tilde(match.matched)}\`.** ${match.note}`);
  else if (match?.inside) parts.push(`> \`${tilde(match.path)}\` is inside \`${tilde(match.matched)}\`.`);
  parts.push(...folder.summary);
  parts.push("## Where it is", folder.paths.map((p) => `\`${p}\``).join("  \n"));
  if (folder.measure?.length)
    parts.push("## How big it is", folder.measure.map((c) => "```\n" + c + "\n```").join("\n\n"));
  parts.push("## How to clear it", folder.how_to_clear);
  if (folder.sources.length) parts.push("## Sources", folder.sources.map((s) => `- [${s.title}](${s.url})`).join("\n"));
  parts.push(`[The full answer on siftmac.com](${folder.url})`);
  return parts.join("\n\n");
}

export function FolderDetail({ folder, match }: { folder: Folder; match?: Match }) {
  const verdict = match?.verdict ?? folder.verdict;
  const label = match?.label ?? folder.verdict_label;
  return (
    <List.Item.Detail
      markdown={folderMarkdown(folder, match)}
      metadata={
        <List.Item.Detail.Metadata>
          <List.Item.Detail.Metadata.TagList title="Verdict">
            <List.Item.Detail.Metadata.TagList.Item text={label} color={COLORS[verdict]} />
          </List.Item.Detail.Metadata.TagList>
          {match && <List.Item.Detail.Metadata.Label title="Matched" text={tilde(match.matched)} />}
          <List.Item.Detail.Metadata.Label title="Category" text={folder.category} />
          {folder.updated && <List.Item.Detail.Metadata.Label title="Answer updated" text={folder.updated} />}
          <List.Item.Detail.Metadata.Separator />
          <List.Item.Detail.Metadata.Link title="Full answer" target={folder.url} text="siftmac.com" />
          <List.Item.Detail.Metadata.Link title="Data" target={REPO_URL} text="Mac Folder Atlas, CC BY 4.0" />
        </List.Item.Detail.Metadata>
      }
    />
  );
}

export function FolderActions({ folder, match }: { folder: Folder; match?: Match }) {
  const command = folder.clear_commands?.[0];
  return (
    <ActionPanel>
      <Action.OpenInBrowser title="Open Full Answer" url={folder.url} />
      {match && exists(match.matched) && <Action.ShowInFinder path={match.matched} />}
      <Action.CopyToClipboard
        title="Copy Path"
        content={match ? tilde(match.matched) : folder.paths[0]}
        shortcut={Keyboard.Shortcut.Common.Copy}
      />
      {command && (
        <Action.CopyToClipboard
          title="Copy Command from the Answer"
          content={command}
          shortcut={{ modifiers: ["cmd", "shift"], key: "k" }}
        />
      )}
      <Action.CopyToClipboard
        title="Copy Link"
        content={folder.url}
        shortcut={{ modifiers: ["cmd", "shift"], key: "l" }}
      />
      <Action.OpenInBrowser
        title="Report a Wrong Answer"
        icon={Icon.Bubble}
        url={`${REPO_URL}/issues/new?title=${encodeURIComponent(`Answer: ${folder.id}`)}`}
      />
    </ActionPanel>
  );
}

export function FolderItem({ folder, match, title }: { folder: Folder; match?: Match; title?: string }) {
  const verdict = match?.verdict ?? folder.verdict;
  const label = match?.label ?? folder.verdict_label;
  return (
    <List.Item
      id={match ? `${folder.id}:${match.path}` : folder.id}
      title={title ?? folder.name}
      subtitle={match ? folder.name : folder.paths[0]}
      keywords={[folder.id, folder.category, ...folder.paths]}
      accessories={[verdictTag(verdict, label)]}
      detail={<FolderDetail folder={folder} match={match} />}
      actions={<FolderActions folder={folder} match={match} />}
    />
  );
}

export function missingIssueUrl(path: string): string {
  return `${REPO_URL}/issues/new?title=${encodeURIComponent(`Add ${tilde(path)}`)}`;
}
