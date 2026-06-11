// DO NOT EDIT — generated from platform/ontology/ops/*.yaml.
// Regen: `python3 platform/codegen/generate.py`.
//
// Typed request/response shapes for the engine's op contract, plus
// the `OpContracts` registry mapping each op wire-name to its pair.

// Named record types — referenced by op req/resp.

export interface Provider {
    /** App id that provides the service. */
    app_id: string;
    /** Tool name (via) on the app that would be invoked. */
    via: string;
    /** Credential state: not_required, present, or missing. */
    cred_state: string;
    /** Optional URL patterns declared on the provides binding. */
    urls?: string[];
}

export interface AuthStoreReadRequest {
    /** Canonical credential-store domain. */
    domain: string;
    /** Credential kind (login_credentials, cookie, oauth, api_key, …). */
    item_type: string;
    /** Optional identifier disambiguator. */
    account?: string;
}

export interface AuthStoreReadResponse {
    /** Whether a matching row exists. */
    found: boolean;
    /** Canonical identifier of the row. */
    identifier?: string;
    /** Decrypted JSON payload; shape depends on item_type. */
    value?: unknown;
    /** Where the row came from (onepassword, brave-browser, …). */
    source?: string;
    /** Unix timestamp of the most recent successful verification. */
    last_verified?: number;
}

export interface BlobsPutRequest {
    /** Base64-encoded bytes to store. */
    data: string;
    /** File extension (no dot), e.g. jpg, ogg, pdf. */
    ext?: string;
}

export interface BlobsPutResponse {
    /** Absolute path of the stored blob. */
    path: string;
    /** SHA-256 of the bytes, hex. */
    sha256: string;
    /** Byte length of the decoded payload. */
    size: number;
}

export interface CryptoPbkdf2Request {
    /** Password to stretch. */
    password: string;
    /** Salt (opaque bytes as a string). */
    salt: string;
    /** Iteration count. */
    iterations?: number;
    /** Desired output length in bytes. */
    length?: number;
}

export type CryptoPbkdf2Response = string;  // Derived key.

export interface CryptoAesRequest {
    /** Key as hex (16 bytes / 32 hex chars for AES-128). */
    key: string;
    /** Ciphertext as hex. */
    data: string;
    /** Initialization vector as hex. Defaults to 32 zero hex chars. */
    iv?: string;
}

export type CryptoAesResponse = string;  // Decrypted plaintext.

export interface HttpRequestRequest {
    /** Absolute URL. */
    url: string;
    /** HTTP method: GET, POST, PUT, DELETE, PATCH, HEAD. */
    method?: string;
    /** Request headers. Cookies ride here under "Cookie". */
    headers?: Record<string, string>;
    /** Query string parameters; appended to the URL. */
    params?: Record<string, unknown>;
    /** Raw request body — bytes or string, sent verbatim. */
    body?: unknown;
    /** Whether to enable HTTP/2. Set false for JA4-fingerprint hosts. */
    http2?: boolean;
    /** Request timeout in seconds. */
    timeout?: number;
}

export interface HttpRequestResponse {
    /** HTTP status code. */
    status: number;
    /** Response body decoded as UTF-8. */
    body?: string;
    /** Hex-encoded response body when non-UTF-8. */
    body_bytes?: string;
    /** Response headers (lowercased keys). */
    headers: Record<string, string>;
    /** Final URL after the redirect chain. */
    url?: string;
    /** Decoded body length in bytes. */
    body_length?: number;
    /** Content encoding (gzip, br, zstd, or none). */
    content_encoding?: string;
}

export interface LlmResolveToolsRequest {
    /** Tool references (app.operation). */
    tools: string[];
}

export interface LlmResolveToolsResponse {
    /** Resolved tool definitions, one per input ref (in order). */
    tools: unknown[];
}

export interface PlistParseRequest {
    /** Hex-encoded plist bytes. */
    hex_data: string;
    /** Extraction map: field_name → object_index in the archived graph. */
    extract: Record<string, number>;
}

export type PlistParseResponse = Record<string, unknown>;  // Extracted fields as field_name → value.

export interface SecretsReadRequest {
    /** Keychain service name. */
    service: string;
    /** Keychain account name; defaults to the current $USER. */
    account?: string;
}

export type SecretsReadResponse = string;  // Secret value as a UTF-8 string.

export interface SecretsReadBinaryRequest {
    /** Keychain service name. */
    service: string;
    /** Keychain account name; defaults to the current $USER. */
    account?: string;
}

export type SecretsReadBinaryResponse = string;  // Binary secret value.

export interface ServicesCallRequest {
    /** Service name to match. */
    name: string;
    /** Tool-name override; defaults to the provider's declared via. */
    verb?: string;
    /** Parameters for the picked tool. Passed through unchanged. */
    params?: unknown;
    /** App-id override; forces a specific provider. */
    app?: string;
}

export type ServicesCallResponse = unknown;  // The picked tool's return value, unchanged — no envelope.

export interface ServicesListProvidersRequest {
    /** Service name to enumerate providers for. */
    name: string;
    /** Optional model filter for llm service matches. */
    model?: string;
}

export interface ServicesListProvidersResponse {
    /** All apps providing `name`, ranked. */
    providers: Provider[];
}

export interface ShellRunRequest {
    /** Binary to execute (absolute path or $PATH name). */
    binary: string;
    /** Argv tail — not shell-parsed. */
    args?: string[];
    /** Timeout in seconds. */
    timeout?: number;
    /** Working directory. Defaults to the process CWD. */
    cwd?: string;
    /** Optional stdin bytes written to the child as UTF-8. */
    input?: string;
}

export interface ShellRunResponse {
    /** Exit code; -1 if the child was signalled. */
    exit_code: number;
    /** Captured stdout (UTF-8 lossy). */
    stdout: string;
    /** Captured stderr (UTF-8 lossy). */
    stderr: string;
}

export interface SqlQueryRequest {
    /** Parameterized SQL text. Use :name placeholders bound via params. */
    sql: string;
    /** Path to the SQLite file. ~ is expanded to $HOME. */
    db: string;
    /** Named bind parameters — mapped onto :name placeholders. */
    params?: Record<string, unknown>;
    /** Alias → path map for ATTACH DATABASE — joins across files. */
    attach?: Record<string, string>;
}

export type SqlQueryResponse = Record<string, unknown>[];  // Rows — each a JSON object keyed by column name.

export interface SqlExecuteRequest {
    /** SQL text to execute. */
    sql: string;
    /** Path to the SQLite file. ~ is expanded to $HOME. */
    db: string;
}

export interface SqlExecuteResponse {
    /** Rows affected by the statement. */
    rows_affected: number;
    /** Rowid of the last INSERT, if applicable. */
    last_insert_rowid?: number;
}

/** Every engine op, keyed by wire name. */
export interface OpContracts {
    "auth_store.read": { request: AuthStoreReadRequest; response: AuthStoreReadResponse };
    "blobs.put": { request: BlobsPutRequest; response: BlobsPutResponse };
    "crypto.pbkdf2": { request: CryptoPbkdf2Request; response: CryptoPbkdf2Response };
    "crypto.aes": { request: CryptoAesRequest; response: CryptoAesResponse };
    "http.request": { request: HttpRequestRequest; response: HttpRequestResponse };
    "llm.resolve_tools": { request: LlmResolveToolsRequest; response: LlmResolveToolsResponse };
    "plist.parse": { request: PlistParseRequest; response: PlistParseResponse };
    "secrets.read": { request: SecretsReadRequest; response: SecretsReadResponse };
    "secrets.read_binary": { request: SecretsReadBinaryRequest; response: SecretsReadBinaryResponse };
    "services.call": { request: ServicesCallRequest; response: ServicesCallResponse };
    "services.list_providers": { request: ServicesListProvidersRequest; response: ServicesListProvidersResponse };
    "shell.run": { request: ShellRunRequest; response: ShellRunResponse };
    "sql.query": { request: SqlQueryRequest; response: SqlQueryResponse };
    "sql.execute": { request: SqlExecuteRequest; response: SqlExecuteResponse };
}

/** Op wire names. */
export type OpName = "auth_store.read" | "blobs.put" | "crypto.pbkdf2" | "crypto.aes" | "http.request" | "llm.resolve_tools" | "plist.parse" | "secrets.read" | "secrets.read_binary" | "services.call" | "services.list_providers" | "shell.run" | "sql.query" | "sql.execute";
