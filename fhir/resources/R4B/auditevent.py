from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/AuditEvent
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class AuditEvent(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event record kept for security purposes.
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """

    __resource_type__ = "AuditEvent"

    action: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="action",
        title="Type of action performed during the event",
        description=(
            "Indicator for type of action performed during the event that generated"
            " the audit."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    action__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_action", title="Extension field for ``action``."
    )

    agent: typing.List[fhirtypes.AuditEventAgentType] = Field(  # type: ignore
        default=...,
        alias="agent",
        title="Actor involved in the event",
        description=(
            "An actor taking an active role in the event or activity that is " "logged."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    entity: typing.List[fhirtypes.AuditEventEntityType] | None = Field(  # type: ignore
        default=None,
        alias="entity",
        title="Data or objects used",
        description="Specific instances of data or objects that have been accessed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    outcome: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="outcome",
        title="Whether the event succeeded or failed",
        description="Indicates whether the event succeeded or failed.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_outcome", title="Extension field for ``outcome``."
    )

    outcomeDesc: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="outcomeDesc",
        title="Description of the event outcome",
        description="A free text description of the outcome of the event.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    outcomeDesc__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_outcomeDesc", title="Extension field for ``outcomeDesc``."
    )

    period: fhirtypes.PeriodType | None = Field(  # type: ignore
        default=None,
        alias="period",
        title="When the activity occurred",
        description="The period during which the activity occurred.",
        json_schema_extra={
            "element_property": True,
        },
    )

    purposeOfEvent: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="purposeOfEvent",
        title="The purposeOfUse of the event",
        description=(
            "The purposeOfUse (reason) that was used during the event being "
            "recorded."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    recorded: fhirtypes.InstantType | None = Field(  # type: ignore
        default=None,
        alias="recorded",
        title="Time when the event was recorded",
        description="The time when the event was recorded.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
        },
    )
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_recorded", title="Extension field for ``recorded``."
    )

    source: fhirtypes.AuditEventSourceType = Field(  # type: ignore
        default=...,
        alias="source",
        title="Audit Event Reporter",
        description="The system that is reporting the event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    subtype: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        default=None,
        alias="subtype",
        title="More specific type/id for the event",
        description="Identifier for the category of event.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    type: fhirtypes.CodingType = Field(  # type: ignore
        default=...,
        alias="type",
        title="Type/identifier of event",
        description=(
            "Identifier for a family of the event.  For example, a menu item, "
            "program, rule, policy, function code, application name or URL. It "
            "identifies the performed function."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AuditEvent`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "type",
            "subtype",
            "action",
            "period",
            "recorded",
            "outcome",
            "outcomeDesc",
            "purposeOfEvent",
            "agent",
            "source",
            "entity",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AuditEvent`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "type",
            "subtype",
            "action",
            "recorded",
            "outcome",
            "outcomeDesc",
            "purposeOfEvent",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("recorded", "recorded__ext")]
        return required_fields


class AuditEventAgent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Actor involved in the event.
    An actor taking an active role in the event or activity that is logged.
    """

    __resource_type__ = "AuditEventAgent"

    altId: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="altId",
        title="Alternative User identity",
        description=(
            "Alternative agent Identifier. For a human, this should be a user "
            "identifier text string from authentication system. This identifier "
            "would be one known to a common authentication system (e.g. single "
            "sign-on), if available."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    altId__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_altId", title="Extension field for ``altId``."
    )

    location: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="location",
        title="Where",
        description="Where the event occurred.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    media: fhirtypes.CodingType | None = Field(  # type: ignore
        default=None,
        alias="media",
        title="Type of media",
        description=(
            "Type of media involved. Used when the event is about "
            "exporting/importing onto media."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Human friendly name for the agent",
        description="Human-meaningful name for the agent.",
        json_schema_extra={
            "element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    network: fhirtypes.AuditEventAgentNetworkType | None = Field(  # type: ignore
        default=None,
        alias="network",
        title="Logical network location for application activity",
        description=(
            "Logical network location for application activity, if the activity has"
            " a network location."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    policy: typing.List[fhirtypes.UriType | None] | None = Field(  # type: ignore
        default=None,
        alias="policy",
        title="Policy that authorized event",
        description=(
            "The policy or plan that authorized the activity being recorded. "
            "Typically, a single activity may have multiple applicable policies, "
            "such as patient consent, guarantor funding, etc. The policy would also"
            " indicate the security token used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    policy__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        default=None, alias="_policy", title="Extension field for ``policy``."
    )

    purposeOfUse: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="purposeOfUse",
        title="Reason given for this user",
        description=(
            "The reason (purpose of use), specific to this agent, that was used "
            "during the event being recorded."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    requestor: bool | None = Field(  # type: ignore
        default=None,
        alias="requestor",
        title="Whether user is initiator",
        description=(
            "Indicator that the user is or is not the requestor, or initiator, for "
            "the event being audited."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            "element_required": True,
        },
    )
    requestor__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_requestor", title="Extension field for ``requestor``."
    )

    role: typing.List[fhirtypes.CodeableConceptType] | None = Field(  # type: ignore
        default=None,
        alias="role",
        title="Agent role in the event",
        description=(
            "The security role that the user was acting under, that come from local"
            " codes defined by the access control security system (e.g. RBAC, ABAC)"
            " used in the local context."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="How agent participated",
        description=(
            "Specification of the participation type the user plays when performing"
            " the event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    who: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="who",
        title="Identifier of who",
        description="Reference to who this agent is that was involved in the event.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "PractitionerRole",
                "Practitioner",
                "Organization",
                "Device",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AuditEventAgent`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "role",
            "who",
            "altId",
            "name",
            "requestor",
            "location",
            "policy",
            "media",
            "network",
            "purposeOfUse",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AuditEventAgent`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "who", "requestor"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("requestor", "requestor__ext")]
        return required_fields


class AuditEventAgentNetwork(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Logical network location for application activity.
    Logical network location for application activity, if the activity has a
    network location.
    """

    __resource_type__ = "AuditEventAgentNetwork"

    address: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="address",
        title="Identifier for the network access point of the user device",
        description=(
            "An identifier for the network access point of the user device for the "
            "audit event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_address", title="Extension field for ``address``."
    )

    type: fhirtypes.CodeType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="The type of network access point",
        description=(
            "An identifier for the type of network access point that originated the"
            " audit event."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_type", title="Extension field for ``type``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AuditEventAgentNetwork`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "address", "type"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AuditEventAgentNetwork`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]


class AuditEventEntity(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Data or objects used.
    Specific instances of data or objects that have been accessed.
    """

    __resource_type__ = "AuditEventEntity"

    description: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="description",
        title="Descriptive text",
        description="Text that describes the entity in more detail.",
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_description", title="Extension field for ``description``."
    )

    detail: typing.List[fhirtypes.AuditEventEntityDetailType] | None = Field(  # type: ignore
        default=None,
        alias="detail",
        title="Additional Information about the entity",
        description=(
            "Tagged value pairs for conveying additional information about the "
            "entity."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    lifecycle: fhirtypes.CodingType | None = Field(  # type: ignore
        default=None,
        alias="lifecycle",
        title="Life-cycle stage for the entity",
        description="Identifier for the data life-cycle stage for the entity.",
        json_schema_extra={
            "element_property": True,
        },
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="name",
        title="Descriptor for entity",
        description="A name of the entity in the audit event.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_name", title="Extension field for ``name``."
    )

    query: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        default=None,
        alias="query",
        title="Query parameters",
        description="The query parameters for a query-type entities.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
        },
    )
    query__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_query", title="Extension field for ``query``."
    )

    role: fhirtypes.CodingType | None = Field(  # type: ignore
        default=None,
        alias="role",
        title="What role the entity played",
        description=(
            "Code representing the role the entity played in the event being "
            "audited."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    securityLabel: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        default=None,
        alias="securityLabel",
        title="Security labels on the entity",
        description="Security labels for the identified entity.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodingType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Type of entity involved",
        description="The type of the object that was involved in this audit event.",
        json_schema_extra={
            "element_property": True,
        },
    )

    what: fhirtypes.ReferenceType | None = Field(  # type: ignore
        default=None,
        alias="what",
        title="Specific instance of resource",
        description=(
            "Identifies a specific instance of the entity. The reference should be "
            "version specific."
        ),
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AuditEventEntity`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "what",
            "type",
            "role",
            "lifecycle",
            "securityLabel",
            "name",
            "description",
            "query",
            "detail",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AuditEventEntity`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "what", "name", "query"]


class AuditEventEntityDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Additional Information about the entity.
    Tagged value pairs for conveying additional information about the entity.
    """

    __resource_type__ = "AuditEventEntityDetail"

    type: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="Name of the property",
        description="The type of extra detail provided in the value.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_type", title="Extension field for ``type``."
    )

    valueBase64Binary: fhirtypes.Base64BinaryType | None = Field(  # type: ignore
        default=None,
        alias="valueBase64Binary",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueString: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="valueString",
        title="Property value",
        description="The  value of the extra detail.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AuditEventEntityDetail`` according to specification,
        with preserving the original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueString",
            "valueBase64Binary",
        ]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AuditEventEntityDetail`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension"]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("type", "type__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"value": ["valueBase64Binary", "valueString"]}
        return one_of_many_fields


class AuditEventSource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Audit Event Reporter.
    The system that is reporting the event.
    """

    __resource_type__ = "AuditEventSource"

    observer: fhirtypes.ReferenceType = Field(  # type: ignore
        default=...,
        alias="observer",
        title="The identity of source detecting the event",
        description="Identifier of the source where the event was detected.",
        json_schema_extra={
            "element_property": True,
            "summary_element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "PractitionerRole",
                "Practitioner",
                "Organization",
                "Device",
                "Patient",
                "RelatedPerson",
            ],
        },
    )

    site: fhirtypes.StringType | None = Field(  # type: ignore
        default=None,
        alias="site",
        title="Logical source location within the enterprise",
        description=(
            "Logical source location within the healthcare enterprise network.  For"
            " example, a hospital or other provider location within a multi-entity "
            "provider group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    site__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        default=None, alias="_site", title="Extension field for ``site``."
    )

    type: typing.List[fhirtypes.CodingType] | None = Field(  # type: ignore
        default=None,
        alias="type",
        title="The type of source where event originated",
        description="Code specifying the type of source where event originated.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all element names from
        ``AuditEventSource`` according to specification,
        with preserving the original sequence order.
        """
        return ["id", "extension", "modifierExtension", "site", "observer", "type"]

    @classmethod
    def summary_elements_sequence(cls):
        """returning all element names (those have summary mode are enabled) from ``AuditEventSource`` according to specification,
        with preserving the original sequence order.
        """
        return ["modifierExtension", "observer"]
