// Auto-generated from shape YAML — do not edit.
// Generated from 72 shapes.
// Regenerate with: python generate.py --lang typescript

export interface Account {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accountType?: string;
    authenticated?: boolean;
    bio?: string;
    color?: string;
    customerId?: string;
    display?: string;
    displayName?: string;
    email?: string;
    handle?: string;
    identifier?: string;
    isActive?: boolean;
    isPrime?: boolean;
    joinedDate?: string;
    lastActive?: string;
    marketplaceId?: string;
    phone?: string;
    redirect?: string;
    statusCode?: number;
    at?: Actor;
    authenticatedVia?: Account;
    followers?: Account[];
    follows?: Account[];
    operator?: Actor;
    owner?: Person;
    previousIdentity?: Account[];
    protocol?: Protocol;
    via?: Product;
}

export interface Activity {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    action?: string;
    changedKeys?: string[];
    duration?: number;
    published?: string;
    success?: boolean;
    toolName?: string;
    folder?: Folder;
    session?: McpSession;
}

export interface Actor {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actorType?: string;
}

export interface Agent {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actorType?: string;
    model?: string;
    provider?: string;
    sessionId?: string;
}

export interface Aircraft {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    availability?: string;
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    currency?: string;
    customizationGroups?: unknown;
    department?: string;
    iataCode?: string;
    icaoCode?: string;
    images?: unknown;
    model?: string;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    rangeKm?: number;
    seatCapacity?: number;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    variant?: string;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    brand?: Brand;
    manufacturer?: Organization;
    tagged?: Tag[];
}

export interface Album {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    contains?: Image[];
}

export interface App {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    appId?: string;
    description?: string;
    entityTypes?: unknown;
    standalone?: boolean;
}

export interface Book {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    availability?: string;
    awardsWon?: string[];
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    characters?: string[];
    currency?: string;
    customizationGroups?: unknown;
    department?: string;
    format?: string;
    genres?: string[];
    images?: unknown;
    isbn?: string;
    isbn13?: string;
    language?: string;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    originalTitle?: string;
    pages?: number;
    places?: string[];
    price?: string;
    priceAmount?: number;
    quantity?: number;
    series?: string;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    brand?: Brand;
    contributors?: Person[];
    manufacturer?: Organization;
    publisher?: Organization;
    tagged?: Tag[];
    writtenBy?: Person;
}

export interface Branch {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    ahead?: number;
    behind?: number;
    commit?: string;
    isCurrent?: boolean;
    isRemote?: boolean;
    upstream?: string;
    repository?: Repository;
}

export interface Brand {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    country?: string;
    founded?: string;
    tagline?: string;
    ownedBy?: Organization;
    website?: Website;
}

export interface Calendar {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accessRole?: string;
    backgroundColor?: string;
    calendarId?: string;
    color?: string;
    foregroundColor?: string;
    isPrimary?: boolean;
    isReadonly?: boolean;
    source?: string;
    timezone?: string;
    at?: Actor;
    events?: Event[];
    owner?: Person;
}

export interface Channel {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    banner?: string;
    subscriberCount?: number;
    at?: Actor;
}

export interface Class {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    activityType?: string;
    allDay?: boolean;
    articleUrl?: string;
    capacity?: number;
    crewIds?: string[];
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    eventType?: string;
    flightNumber?: number;
    icalUid?: string;
    isFull?: boolean;
    landingOutcomes?: unknown;
    launchpadId?: string;
    patchImage?: string;
    properties?: unknown;
    recurrence?: string[];
    reusedBoosters?: string[];
    rocketId?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    spotsRemaining?: number;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
    webcastUrl?: string;
    wikipediaUrl?: string;
    at?: Actor;
    attachments?: File[];
    creator?: Person;
    instructor?: Person;
    involves?: Person[];
    location?: Place;
    organizer?: Person;
    person?: Person;
    venue?: Place;
}

export interface Community {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allowCrypto?: boolean;
    memberCount?: number;
    privacy?: string;
    subscriberCount?: number;
    at?: Actor;
}

export interface Conversation {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accountEmail?: string;
    cwd?: string;
    gitBranch?: string;
    historyId?: string;
    isArchived?: boolean;
    isGroup?: boolean;
    messageCount?: number;
    source?: string;
    unreadCount?: number;
    at?: Actor;
    in?: Folder;
    message?: Message[];
    participant?: Actor[];
}

export interface DnsRecord {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    domain?: string;
    priority?: number;
    recordId?: string;
    recordName?: string;
    recordType?: string;
    ttl?: number;
    type?: string;
    values?: string[];
}

export interface Document {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    abstract?: string;
    contentType?: string;
    encoding?: string;
    filename?: string;
    format?: string;
    kind?: string;
    language?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    sha?: string;
    size?: number;
    tableOfContents?: string;
    wordCount?: number;
    attachedTo?: Message;
    author?: Actor;
    citedBy?: Document[];
    references?: Document[];
    repository?: Repository;
}

export interface Domain {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    autoRenew?: boolean;
    createdAt?: string;
    expiresAt?: string;
    nameservers?: string[];
    registrar?: string;
    status?: string;
}

export interface Email {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accountEmail?: string;
    attachments?: unknown;
    authResults?: string;
    bccRaw?: string;
    bodyHtml?: string;
    ccRaw?: string;
    conversationId?: string;
    deliveredTo?: string;
    draftId?: string;
    hasAttachments?: boolean;
    inReplyTo?: string;
    isAutomated?: boolean;
    isDraft?: boolean;
    isOutgoing?: boolean;
    isSent?: boolean;
    isSpam?: boolean;
    isStarred?: boolean;
    isTrash?: boolean;
    isUnread?: boolean;
    listId?: string;
    mailer?: string;
    manageSubscription?: string;
    messageId?: string;
    precedence?: string;
    references?: string;
    replyTo?: string;
    returnPath?: string;
    sizeEstimate?: number;
    subject?: string;
    toRaw?: string;
    unsubscribe?: string;
    unsubscribeOneClick?: boolean;
    at?: Actor;
    bcc?: Account[];
    cc?: Account[];
    ccDomain?: Domain[];
    domain?: Domain;
    from?: Account;
    inConversation?: Conversation;
    repliesTo?: Message;
    tag?: Tag[];
    to?: Account[];
    toDomain?: Domain[];
    toolCalls?: ToolCall[];
}

export interface Episode {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    durationMs?: number;
    episodeNumber?: number;
    seasonNumber?: number;
    guest?: Person[];
    series?: Podcast;
    transcribe?: Transcript;
}

export interface Event {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allDay?: boolean;
    articleUrl?: string;
    crewIds?: string[];
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    eventType?: string;
    flightNumber?: number;
    icalUid?: string;
    landingOutcomes?: unknown;
    launchpadId?: string;
    patchImage?: string;
    properties?: unknown;
    recurrence?: string[];
    reusedBoosters?: string[];
    rocketId?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
    webcastUrl?: string;
    wikipediaUrl?: string;
    at?: Actor;
    attachments?: File[];
    creator?: Person;
    involves?: Person[];
    location?: Place;
    organizer?: Person;
    person?: Person;
}

export interface File {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    encoding?: string;
    filename?: string;
    format?: string;
    kind?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    sha?: string;
    size?: number;
    attachedTo?: Message;
    repository?: Repository;
}

export interface FinancialAccount {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accountId?: string;
    accountNumber?: string;
    accountType?: string;
    available?: number;
    balance?: number;
    cardType?: string;
    creditLimit?: number;
    currency?: string;
    expiresAt?: string;
    identifier?: string;
    interestRate?: number;
    last4?: string;
    minimumPayment?: number;
    paymentDueDate?: string;
    routingNumber?: string;
    accessedVia?: Account;
    at?: Actor;
    owner?: Person;
}

export interface Folder {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    hasReadme?: boolean;
    path?: string;
    workspaceType?: string;
    contains?: File[];
    repository?: Repository;
}

export interface GitCommit {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    additions?: number;
    committedAt?: string;
    deletions?: number;
    filesChanged?: number;
    message?: string;
    sha?: string;
    shortHash?: string;
    author?: Account;
    committer?: Account;
    parent?: GitCommit;
    repository?: Repository;
}

export interface Group {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    category?: string;
    memberCount?: number;
}

export interface Hardware {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    availability?: string;
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    currency?: string;
    customizationGroups?: unknown;
    department?: string;
    images?: unknown;
    modelNumber?: string;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    serialNumber?: string;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    specs?: unknown;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    brand?: Brand;
    manufacturer?: Organization;
    tagged?: Tag[];
}

export interface Image {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    altText?: string;
    appName?: string;
    displayId?: number;
    displayIndex?: number;
    encoding?: string;
    filename?: string;
    format?: string;
    height?: number;
    kind?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    sha?: string;
    size?: number;
    width?: number;
    windowId?: number;
    attachedTo?: Message;
    repository?: Repository;
}

export interface Invitation {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    acceptedAt?: string;
    email?: string;
    expiresAt?: string;
    invitationType?: string;
    message?: string;
    revokedAt?: string;
    role?: string;
    status?: string;
    token?: string;
    at?: Actor;
    invitee?: Account;
    inviter?: Account;
    organization?: Organization;
}

export interface Job {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    bootEpoch?: number;
    config?: unknown;
    kind?: string;
    status?: string;
    produced?: Conversation;
    requestedBy?: Account;
}

export interface Leg {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    arrivalTime?: string;
    cabinClass?: string;
    carbonEmissions?: unknown;
    departureTime?: string;
    duration?: string;
    durationMinutes?: number;
    flightNumber?: string;
    layoverMinutes?: number;
    polyline?: string;
    sequence?: number;
    trace?: unknown;
    tracePointCount?: number;
    vehicleType?: string;
    aircraft?: Aircraft;
    carrier?: Organization;
    destination?: Place;
    origin?: Place;
    trip?: Trip;
}

export interface List {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    isDefault?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    items?: unknown;
    listId?: string;
    listType?: string;
    privacy?: string;
    at?: Actor;
    belongsTo?: Account;
    contains?: Product[];
}

export interface LoadedModel {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    digest?: string;
    expiresAt?: string;
    quantization?: string;
    size?: string;
    sizeVram?: number;
    vramUsage?: string;
}

export interface McpSession {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    client?: string;
    endedAt?: string;
    gitBranch?: string;
    messageCount?: number;
    projectId?: string;
    sessionType?: string;
    startedAt?: string;
    tokenCount?: number;
    folder?: Folder;
    participant?: Actor;
}

export interface Meeting {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allDay?: boolean;
    articleUrl?: string;
    calendarLink?: string;
    conferenceProvider?: string;
    crewIds?: string[];
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    eventType?: string;
    flightNumber?: number;
    icalUid?: string;
    isVirtual?: boolean;
    landingOutcomes?: unknown;
    launchpadId?: string;
    meetingUrl?: string;
    patchImage?: string;
    phoneDialIn?: string;
    properties?: unknown;
    recurrence?: string[];
    reusedBoosters?: string[];
    rocketId?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
    webcastUrl?: string;
    wikipediaUrl?: string;
    at?: Actor;
    attachments?: File[];
    creator?: Person;
    involves?: Person[];
    location?: Place;
    organizer?: Person;
    person?: Person;
    transcribe?: Transcript;
}

export interface Membership {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    autoRenew?: boolean;
    billingType?: string;
    currency?: string;
    endEffectiveDate?: string;
    guestPassQuantity?: number;
    nextBillDate?: string;
    price?: number;
    startEffectiveDate?: string;
    status?: string;
    tier?: string;
    useCount?: number;
    account?: Account;
    at?: Actor;
    location?: Place;
    member?: Person;
    plan?: Product;
}

export interface Memex {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    description?: string;
    edgeCount?: number;
    filePath?: string;
    fileSize?: string;
    nodeCount?: number;
    origin?: string;
    published?: boolean;
    snapshotOf?: string;
    forkedFrom?: Memex;
    owner?: Person;
    snapshots?: Memex[];
}

export interface Message {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    conversationId?: string;
    isOutgoing?: boolean;
    isStarred?: boolean;
    at?: Actor;
    from?: Actor;
    inConversation?: Conversation;
    repliesTo?: Message;
    toolCalls?: ToolCall[];
}

export interface Model {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    contextLength?: number;
    contextWindow?: number;
    digest?: string;
    family?: string;
    format?: string;
    maxOutput?: number;
    modality?: string[];
    modelType?: string;
    parameterSize?: string;
    pricingInput?: string;
    pricingOutput?: string;
    quantization?: string;
    quantizationLevel?: string;
    size?: string;
    at?: Actor;
}

export interface Note {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    isPinned?: boolean;
    noteType?: string;
    createdBy?: Person;
    extractedFrom?: Webpage;
    references?: Note[];
}

export interface Offer {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    availability?: string;
    bookingToken?: string;
    currency?: string;
    departureToken?: string;
    offerType?: string;
    price?: number;
    validFrom?: string;
    validUntil?: string;
    for?: Product;
    offeredBy?: Organization;
    trips?: Trip[];
}

export interface Order {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    body?: string;
    currency?: string;
    deliveryDate?: string;
    deliveryFee?: number;
    deliveryInstructions?: string;
    eta?: string;
    fareBreakdown?: unknown;
    head?: string;
    interactionType?: string;
    itemStates?: unknown;
    latestArrival?: string;
    messages?: unknown;
    orderDate?: string;
    orderId?: string;
    orderUuid?: string;
    originalTotal?: string;
    originalTotalAmount?: number;
    progress?: number;
    progressTotal?: number;
    savings?: number;
    status?: string;
    subtotal?: number;
    summary?: string;
    taxes?: number;
    timeline?: unknown;
    tipAmount?: number;
    total?: string;
    totalAmount?: number;
    at?: Actor;
    contains?: Product[];
    delivery?: Trip;
    shippingAddress?: Place;
    store?: Place;
    tracking?: Webpage;
}

export interface Organization {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actorType?: string;
    founded?: string;
    industry?: string;
    domain?: Domain;
    headquarters?: Place;
    member?: Person[];
    website?: Website;
}

export interface Pass {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    currency?: string;
    depletedDate?: string;
    endEffectiveDate?: string;
    isAllDayPass?: boolean;
    price?: number;
    purchasedDate?: string;
    purchasedQuantity?: number;
    quantity?: number;
    startEffectiveDate?: string;
    status?: string;
    useCount?: number;
    account?: Account;
    at?: Actor;
    grantedBy?: Membership;
    holder?: Person;
    location?: Place;
    type?: Product;
}

export interface Person {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    about?: string;
    actorType?: string;
    birthday?: string;
    browser?: string;
    distinctIds?: string[];
    email?: string;
    firstName?: string;
    gender?: string;
    initialReferrer?: string;
    initialUtmSource?: string;
    joinedDate?: string;
    lastActive?: string;
    lastName?: string;
    lastSeenAt?: string;
    middleName?: string;
    nickname?: string;
    notes?: string;
    os?: string;
    accounts?: Account[];
    location?: Place;
    memberships?: Membership[];
    passes?: Pass[];
    roles?: Role[];
    website?: Website;
}

export interface Place {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accuracy?: string;
    businessStatus?: string;
    categories?: string[];
    city?: string;
    closedMessage?: string;
    country?: string;
    countryCode?: string;
    district?: string;
    eta?: string;
    featureType?: string;
    fullAddress?: string;
    googlePlaceId?: string;
    hours?: unknown;
    isOrderable?: boolean;
    latitude?: number;
    locality?: string;
    longitude?: number;
    mapboxId?: string;
    neighborhood?: string;
    phone?: string;
    placeFormatted?: string;
    postalCode?: string;
    priceLevel?: string;
    productCount?: number;
    rating?: number;
    region?: string;
    reviewCount?: number;
    street?: string;
    streetNumber?: string;
    timezone?: string;
    website?: string;
    wikidataId?: string;
    at?: Actor;
    brand?: Organization;
    offers?: Product[];
}

export interface Playlist {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    isDefault?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    items?: unknown;
    listId?: string;
    listType?: string;
    privacy?: string;
    at?: Actor;
    belongsTo?: Account;
    contains?: Video[];
}

export interface Podcast {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    feedUrl?: string;
    at?: Actor;
    episode?: Episode[];
    host?: Person[];
}

export interface Post {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    commentCount?: number;
    community?: string;
    externalUrl?: string;
    postType?: string;
    score?: number;
    at?: Actor;
    attachment?: File[];
    contains?: Video[];
    media?: Image[];
    postedBy?: Account;
    publish?: Community;
    replies?: Post[];
    repliesTo?: Post;
}

export interface Product {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    availability?: string;
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    currency?: string;
    customizationGroups?: unknown;
    department?: string;
    images?: unknown;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    brand?: Brand;
    manufacturer?: Organization;
    tagged?: Tag[];
}

export interface Project {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    color?: string;
    parentId?: string;
    state?: string;
    at?: Actor;
}

export interface Protocol {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    homepage?: string;
    rfc?: string;
    wikidataId?: string;
}

export interface Quote {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    context?: string;
    year?: number;
}

export interface Repository {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    defaultBranch?: string;
    forks?: number;
    isArchived?: boolean;
    isPrivate?: boolean;
    language?: string;
    license?: string;
    openIssues?: number;
    size?: number;
    stars?: number;
    topics?: string[];
    forkedFrom?: Repository;
    owner?: Account;
}

export interface Result {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    community?: string;
    externalUrl?: string;
    indexedAt?: string;
    postId?: string;
    resultType?: string;
    score?: number;
    similarity?: number;
}

export interface Review {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    commentCount?: number;
    community?: string;
    externalUrl?: string;
    isVerified?: boolean;
    postType?: string;
    rating?: number;
    ratingMax?: number;
    score?: number;
    tags?: string[];
    at?: Actor;
    attachment?: File[];
    contains?: Video[];
    media?: Image[];
    postedBy?: Account;
    publish?: Community;
    replies?: Post[];
    repliesTo?: Post;
    reviews?: Product;
}

export interface Role {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    department?: string;
    endDate?: string;
    roleType?: string;
    startDate?: string;
    title?: string;
    organization?: Organization;
    person?: Person;
}

export interface Shelf {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    isDefault?: boolean;
    isExclusive?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    items?: unknown;
    listId?: string;
    listType?: string;
    privacy?: string;
    at?: Actor;
    belongsTo?: Account;
    contains?: Book[];
}

export interface Simulation {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actionCount?: number;
    endedAt?: string;
    graphMode?: string;
    profile?: string;
    startedAt?: string;
    status?: string;
    task?: string;
    writeCount?: number;
    agent?: Agent;
    forkedFrom?: Simulation;
    mountedMemex?: Memex[];
    primaryMemex?: Memex;
    startedBy?: Person;
    tether?: Hardware;
}

export interface Skill {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    color?: string;
    description?: string;
    error?: string;
    skillId?: string;
    status?: string;
    privacyPolicy?: Webpage;
    termsOfService?: Webpage;
    website?: Website;
}

export interface Source {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    address?: string;
    description?: string;
    enabled?: boolean;
    lastSynced?: string;
    scanner?: string;
    sourceId?: string;
    folder?: Folder;
}

export interface Spec {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    encoding?: string;
    filename?: string;
    format?: string;
    kind?: string;
    labels?: string[];
    lineCount?: number;
    mimeType?: string;
    parentId?: string;
    path?: string;
    priority?: number;
    problem?: string;
    projectId?: string;
    remoteId?: string;
    sha?: string;
    size?: number;
    startedAt?: string;
    state?: string;
    successCriteria?: string;
    target?: unknown;
    targetDate?: string;
    assignedTo?: Person;
    at?: Actor;
    attachedTo?: Message;
    blockedBy?: Task[];
    blocks?: Task[];
    children?: Task[];
    dependsOn?: Spec[];
    parent?: Task;
    project?: Project;
    repository?: Repository;
    supersedes?: Spec[];
}

export interface Tag {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    annotated?: boolean;
    color?: string;
    hash?: string;
    tagType?: string;
}

export interface Task {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    labels?: string[];
    parentId?: string;
    priority?: number;
    projectId?: string;
    remoteId?: string;
    startedAt?: string;
    state?: string;
    target?: unknown;
    targetDate?: string;
    assignedTo?: Person;
    at?: Actor;
    blockedBy?: Task[];
    blocks?: Task[];
    children?: Task[];
    parent?: Task;
    project?: Project;
    repository?: Repository;
}

export interface Theme {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    colorScheme?: string;
    description?: string;
    family?: string;
    themeId?: string;
    wallpaper?: Image;
}

export interface ToolCall {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    durationMs?: number;
    input?: string;
    isError?: boolean;
    output?: string;
    from?: Actor;
    inMessage?: Message;
    platform?: Product;
    repliesTo?: ToolCall;
}

export interface Transaction {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    amount?: number;
    balance?: number;
    category?: string;
    currency?: string;
    details?: unknown;
    notes?: string;
    pending?: boolean;
    postingDate?: string;
    recurring?: boolean;
    type?: string;
    account?: FinancialAccount;
    at?: Actor;
}

export interface Transcript {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    contentRole?: string;
    durationMs?: number;
    language?: string;
    segmentCount?: number;
    segments?: unknown;
    sourceType?: string;
}

export interface Trip {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    arrivalTime?: string;
    bookingToken?: string;
    cabinClass?: string;
    carbonEmissions?: unknown;
    currency?: string;
    departureTime?: string;
    distance?: string;
    duration?: string;
    durationMinutes?: number;
    fare?: string;
    fareAmount?: number;
    guest?: unknown;
    isPool?: boolean;
    isReserve?: boolean;
    isScheduled?: boolean;
    isSurge?: boolean;
    marketplace?: string;
    rating?: string;
    status?: string;
    stops?: number;
    trackingUrl?: string;
    tripType?: string;
    vehicle?: unknown;
    vehicleType?: string;
    at?: Actor;
    carrier?: Organization;
    destination?: Place;
    driver?: Person;
    legs?: Leg[];
    order?: Order;
    origin?: Place;
}

export interface Video {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    codec?: string;
    durationMs?: number;
    encoding?: string;
    filename?: string;
    format?: string;
    frameRate?: number;
    kind?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    resolution?: string;
    sha?: string;
    size?: number;
    viewCount?: number;
    addTo?: Playlist;
    attachedTo?: Message;
    channel?: Channel;
    repository?: Repository;
    transcribe?: Transcript;
}

export interface Webpage {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    contentType?: string;
    error?: string;
    lastVisitUnix?: number;
    visitCount?: number;
}

export interface Website {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    anonymous?: boolean;
    claimToken?: string;
    claimUrl?: string;
    expiresAt?: string;
    status?: string;
    versionId?: string;
    domain?: Domain;
    ownedBy?: Organization;
}
